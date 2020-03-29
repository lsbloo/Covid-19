#!/bin/bash


echo 'Running....'
echo ''
echo 'Memoria Fisica.'

df -B GB | grep /dev/sda2

sleep 2

echo ''
echo 'Memoria RAM'
free -m
echo ''
echo 'Negócio ta ruim pra tu....'
