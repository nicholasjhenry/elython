# Elixir and Python Integration: "Elython"

Integration using [Pyrlang](https://pyrlang.github.io/Pyrlang/): Erlang node implemented in Python 3.5+ (Asyncio-based).

## References

- [Deploying Machine Learning Models for Elixir applications #1: Getting Started](https://medium.com/@pawel_dawczak/elixir-python-1-getting-started-165317f873fa)
- [Deploying Machine Learning Models for Elixir applications #2: Getting Excited](https://medium.com/@pawel_dawczak/elixir-python-2-getting-excited-672ec35fa681)

## Prerequistes

Docker only.

## Setup

    $ make build

## Demo

Start up two separate shells:

    # Shell 1: start up an Elixir shell and register the shell process
    $ make demo.start
    iex> Process.register(self(), :iex)
    
    # Shell 2: send a message `:hello` from Python to the Elixir shell (demo.py)
    $ make demo.send_message

    # Shell 1: flush the shell/process mailbox to view the message `:hello`
    iex> flush

## Tips

Ctrl-C to exit the Elixir shell and Python process.
