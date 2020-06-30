# Time's Up, Again!

First we need to implement a fast calulator. This need to be fast as hell, so
you're options are c, c++, rust. I chose rust, as it has way nices methods of 
dealing with the process.

```rust
struct Solver<'a> {
    pub prob: &'a [u8],
}

impl<'a> Solver<'a> {
    fn new(prob: &'a [u8]) -> Self {
        Self { prob }
    }

    fn peek(&self) -> u8 {
        *self.prob.get(0).unwrap_or(&0)
    }

    fn get(&mut self) -> u8 {
        let ret = self.peek();
        self.prob = &self.prob[1..];
        ret
    }

    fn number(&mut self) -> i64 {
        let mut ret: i64 = (self.get() - b'0') as i64;
        while self.peek() >= b'0' && self.peek() <= b'9' {
            ret = 10 * ret + (self.get() - b'0') as i64;
        }
        ret
    }

    fn factor(&mut self) -> i64 {
        if self.peek() >= b'0' && self.peek() <= b'9' {
            self.number()
        } else if self.peek() == b'(' {
            self.get();
            let ret = self.expr();
            self.get();
            ret
        } else if self.peek() == b'-' {
            self.get();
            return -self.factor();
        } else {
            unreachable!(
                "{},{}",
                self.peek() as char,
                std::str::from_utf8(self.prob).unwrap()
            )
        }
    }

    fn term(&mut self) -> i64 {
        let mut res = self.factor();
        while self.peek() == b'*' || self.peek() == b'/' {
            if self.get() == b'*' {
                res *= self.factor()
            } else {
                res /= self.factor()
            }
        }
        res
    }

    fn expr(&mut self) -> i64 {
        let mut res = self.term();
        while self.peek() == b'+' || self.peek() == b'-' {
            if self.get() == b'+' {
                res += self.term()
            } else {
                res -= self.term()
            }
        }
        res
    }
}
```

This uses [recursive decent](https://stackoverflow.com/questions/9329406/evaluating-arithmetic-expressions-from-string-in-c), and doesn't build up a tree, but evals right away, so it's fast.

Now we can get on with the ipc.

```rust
const DIR: &str = "/problems/time-s-up--again-_6_3b092353ed59a3db99109f8c0f6f5cd0/";
const COMMAND: &str =
    "/problems/time-s-up--again-_6_3b092353ed59a3db99109f8c0f6f5cd0/times-up-again";

fn main() {
    let mut process = Command::new(COMMAND)
        .current_dir(DIR)
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped())
        .spawn()
        .unwrap();
```
Then we pull the stdin and stdout. This is much nicer than dealing with libc
```rust
    let answer = process.stdin.as_mut().unwrap();
    let mut question = BufReader::new(process.stdout.as_mut().unwrap());
    let mut buff = String::new();
```
Then we read the question, remove the header and spacer, solver it, and create the responce
```rust
    question.read_line(&mut buff).unwrap();
    let q = &buff["Challenge: ".len()..buff.len()];

    let q = q.replace(" ", "");

    let mut solver = Solver::new(q.as_bytes());

    let mut ans = solver.expr().to_string();
    ans.push('\n');
```
Finaly we send the responce and record the flag
```rust
    answer.write(ans.as_bytes());

    question.read_line(&mut buff).unwrap();

    question.read_line(&mut buff).unwrap();
    println!("{}", buff);
}
```
They don't have rustc on the server, but the binary is static, so we can just copy it over
```
cargo build --release
strip target/release/solve
scp target/release/solve yeswriteup@2019shell1.picoctf.com:~
```

Flag: `picoCTF{Hasten. Hurry. Ferrociously Speedy. #2edc7d0a}`