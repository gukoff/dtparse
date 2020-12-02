extern crate pyo3;

extern crate chrono;

use chrono::prelude::*;
use pyo3::exceptions::*;
use pyo3::prelude::*;
use pyo3::types::*;

// https://pyo3.rs/v0.12.4/module.html
// This macro makes Rust compile a _dtparse.so binary in Python-compatible format.
// Such a binary can be imported from Python just like a regular Python module.
#[pymodule(_dtparse)]
fn init_mod(_py: Python, m: &PyModule) -> PyResult<()> {
    // We fill this module with everything we want to make visible from Python.

    #[pyfn(m, "parse")]
    fn parse(_py: Python, str_datetime: String, fmt: String) -> PyResult<&PyDateTime> {
        // Call chrono and ask it to parse the datetime for us
        let chrono_dt = Utc.datetime_from_str(str_datetime.as_str(), fmt.as_str());

        // In case chrono couldn't parse a datetime, raise a ValueError with chrono's error message.
        // Because there are no exceptions in Rust, we return a PyValueError instance here.
        // By convention, it will make PyO3 wrapper raise an exception in Python interpreter.
        // https://pyo3.rs/v0.12.4/exception.html
        if chrono_dt.is_err() {
            return Err(PyValueError::new_err(
                chrono_dt.err().unwrap().to_string().to_owned(),
            ));
        }

        // In case everything's fine, get Rust datetime out of the result and transform
        // it into a Python datetime.
        let dt = chrono_dt.unwrap();
        let result = PyDateTime::new(
            _py,
            dt.year(),
            dt.month() as u8,
            dt.day() as u8,
            dt.hour() as u8,
            dt.minute() as u8,
            dt.second() as u8,
            0,
            None,
        );
        Ok(result?)
    }

    Ok(())
}
