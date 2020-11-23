#!/bin/bash

# カレントディレクトリをスクリプトのあるディレクトリに変更
cd `dirname $0`

# path to pipenv
exec /home/dev/.anyenv/envs/pyenv/shims/pipenv run start

# バックグラウンドプロセスのプロセスIDを表示
echo $!
