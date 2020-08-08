#!/bin/bash

# カレントディレクトリをスクリプトのあるディレクトリに変更
cd `dirname $0`

pipenv run start &

# バックグラウンドプロセスのプロセスIDを表示
echo $!
