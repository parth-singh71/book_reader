# Book Reader

A piece of code to listen to books with some voice commands on your linux pc.

## PyAudio Installation

[PyAudio](https://pypi.org/project/PyAudio/), the cross-platform audio input/output stream library is needed for this to work.

### For Ubuntu or Debian users

```shell
$ sudo apt-get install python-pyaudio python3-pyaudio
$ pip install PyAudio
```

### For Windows users

```shell
$ pip install PyAudio
```

## Quick Setup

You can quickly download the dependencies using the command given below.

```shell
pip install -r requirements.txt
```

## Getting Started

### For listening a single page

```shell
python main.py --pdf 'pdf_name.pdf' --single --page 10
```

### For listening multiple pages

```shell
python main.py --pdf 'pdf_name.pdf' --multi
```

#### Other examples

```shell
python main.py --pdf 'storybook.pdf' --multi --from_page 8
```

```shell
python main.py --pdf 'chapter2.pdf' --multi --from_page 45
```
