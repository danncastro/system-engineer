#!/bin/bash

for resolver in $(echo x.x.x.x x.x.x.x x.x.x.x); do echo -n "testando resolver $resolver \n" && dig A uolhost.uol.com.br @$resolver +short ;done