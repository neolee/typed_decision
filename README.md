# Typed Decision Making, Locally

Test bed and playground for running typed decision model like [laya](https://github.com/NandhaKishorM/laya).

## Environment Pre-requisites

- Apple silicon Mac
- macOS 14+
- Python 3.11+

My setup:
- Apple M1 Max + 32 GB Unified Memory
- macOS 27.0
- Python 3.11.16
- uv 0.12.18

## Getting Started

1. Clone this repo.

2. Install [laya-mlx](https://github.com/mizorewww/laya-mlx/) with demo and [laya-multilingual-mlx](https://huggingface.co/aac6fef/laya-multilingual-mlx) network weights:

``` shell
uv sync
hf download aac6fef/laya-multilingual-mlx
```

3. Run basic decision test (source code at [src/typed_decision/cli.py](src/typed_decision/cli.py)):

``` shell
uv run typed-decision
```

4. Run the laya-snake demo:

``` shell
uv run laya-snake --optimize --max-speed
```

## Acknowledge

- [TypeSafe Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev): for making this approach popular.
- [laya](https://github.com/NandhaKishorM/laya): for a sold base of open source typed decision engine.
- [laya-mlx](https://github.com/mizorewww/laya-mlx): for migrating laya to Apple silicon.
