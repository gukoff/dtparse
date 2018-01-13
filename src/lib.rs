#![feature(proc_macro, specialization, const_fn)]
#![feature(const_fn, const_align_of, const_size_of, const_ptr_null, const_ptr_null_mut)]
extern crate pyo3;

extern crate chrono;

use chrono::prelude::*;
use pyo3::prelude::*;
use std::error::Error;


// https://pyo3.github.io/pyo3/guide/class.html#define-new-class
// py::class macro transforms a Rust's Parser struct into a Python class
#[py::class]
struct Parser {
    // we keep the datetime class in the structure, because we can't import it into the global
    // scope in Rust. We should either accept it in constructor, or accept it as a parameter
    // for parse, or import it at runtime. This looks like the most sensible way of three.
    datetime_class: PyObject,
    // token is needed to create a "rich" Python class, which has access to Python interpreter.
    token: PyToken,
}


// https://pyo3.github.io/pyo3/guide/class.html#instance-methods
// py::methods macro generates Python-compatible wrappers for functions in the impl block.
#[py::methods]
impl Parser {
    // https://pyo3.github.io/pyo3/guide/class.html#constructor
    // Constructor is not created by default.
    #[new]
    fn __new__(obj: &PyRawObject, datetime_class: PyObject) -> PyResult<()> {
        obj.init(| token|
            Parser { datetime_class, token }
        )
    }

    // This function will be transformed into a Python method.
    // It has a special argument py: Python. If specified, it gets passed by PyO3 implicitly.
    // It contains the Python interpreter - we're going to use it to create Python objects.
    fn parse(&self, py: Python, str_datetime: String, fmt: String) -> PyResult<PyObject> {
        // Call chrono and ask it to parse the datetime for us
        let result = Utc.datetime_from_str(
            str_datetime.as_str(), fmt.as_str()
        );

        // In case chrono couldn't parse datetime, raise a ValueError with chrono's error message.
        // Because there are no exceptions in Rust, we return an exc::ValueError instance here.
        // By convention, it will make PyO3 wrapper raise an exception in Python interpreter.
        // https://pyo3.github.io/pyo3/guide/exception.html#raise-an-exception
        if result.is_err() {
            return Err(exc::ValueError::new(
                result.err().unwrap().description().to_owned()
            ));
        }

        // In case everything's fine, get Rust datetime out of the result and transform
        // it into a Python datetime. We use Python here to create a tuple of arguments
        // and the datetime itself.
        let dt = result.unwrap();
        let args = PyTuple::new(
            py, &[
                dt.year(),
                dt.month() as i32,
                dt.day() as i32,
                dt.hour() as i32,
                dt.minute() as i32,
                dt.second() as i32,
            ]
        );
        Ok(self.datetime_class.call1(py, args)?)
    }
}


// https://pyo3.github.io/pyo3/guide/module.html
// This macro will make Rust compile a _dtparse.so binary in Python-compatible format.
// Such binary could be imported in Python just like a normal Python module.
#[py::modinit(_dtparse)]
fn init_mod(_py: Python, m: &PyModule) -> PyResult<()> {
    // Here we fill an empty module with everything we want to make visible from Python.
    m.add_class::<Parser>()?;
    Ok(())
}
