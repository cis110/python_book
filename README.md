# Development instructions

## Making a correction to the book

Github allows you to edit files directly on the web. If you notice a typo or mistake that you are sure of, feel free to fix it directly. Alternatively, create an issue and it will be fixed later.

## Expanding the book

1. Create a new `.md` file in `src/`
2. Add it in `src/SUMMARY.md` for it to be displayed

## Locally preview the book
1. Install [Rust.](https://www.rust-lang.org/tools/install)
2. Install `mdbook` like so: `cargo install mdbook`
3. Run `mdbook serve` in the root directory to build the book, launch a preview server, and have the server reload on saved changes. The book will be visible in your browser.
4. You can read more about the `mdbook` tool [here.](https://rust-lang.github.io/mdBook/)

## TODOs:
[ ] Cover Loops, Comprehensions, Functions, sets, dicts, unit-testing ideally keeping pace with the course
