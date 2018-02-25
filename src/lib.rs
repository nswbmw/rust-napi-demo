#[macro_use]
extern crate napi;
#[macro_use]
extern crate napi_derive;

use napi::{NapiEnv, NapiNumber, NapiResult};

#[derive(NapiArgs)]
struct Args<'a> {
  n: NapiNumber<'a>
}

fn fibonacci<'a>(env: &'a NapiEnv, args: &Args<'a>) -> NapiResult<NapiNumber<'a>> {
  let number = args.n.to_i32()?;
  NapiNumber::from_i32(env, _fibonacci(number))
}

napi_callback!(export_fibonacci, fibonacci);

fn _fibonacci(n: i32) -> i32 {
  match n {
    1 | 2 => 1,
    _ => _fibonacci(n - 1) + _fibonacci(n - 2)
  }
}
