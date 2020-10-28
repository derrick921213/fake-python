#!/bin/bash

pymod=flask,

warn()
{
  echo "Warning: $*"
}

found()
{
  echo "$* found"
}

if python -c "import $pymod" >/dev/null 2>&1
then
    found "$pymod"
else
    warn "$pymod: NOT FOUND"
fi