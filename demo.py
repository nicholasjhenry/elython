#
# Start a simple node and connect to an Erlang/Elixir node.
# This Pyrlang node will be visible as `py@127.0.0.1`.
#
# 1. Run `iex --name ex@127.0.0.1 --cookie COOKIE`
# 2. In Elixir shell: `Node.register(self(), :iex).`
#
# Shell process will receive 'hello' (type `flush()` to see)
#
import logging

from pyrlang.node import Node
from term import Atom

LOG = logging.getLogger()


async def example_main(node):
    fake_pid = node.register_new_process()

    # To be able to send to Elixir shell by name first give it a registered
    # name: `Node.register(self(), :iex).`
    # To see an incoming message in shell: `flush().`
    await node.send(sender=fake_pid,
                    receiver=(Atom('ex@127.0.0.1'), Atom('iex')),
                    message=Atom('hello'))
    LOG.info("example_main: Done")


def main():
    node = Node(node_name="py@127.0.0.1", cookie="COOKIE")
    ev = node.get_loop()
    ev.create_task(example_main(node))
    node.run()


if __name__ == "__main__":
    main()