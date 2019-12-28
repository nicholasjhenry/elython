# Elixir and Python Integration: "Elython"

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
