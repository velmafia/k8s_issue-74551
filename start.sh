#!/usr/bin/env bash

helm install broken-pipe ./port-forward-broken-pipe/ --wait
sleep 5 # wait extra time for pod
kubectl port-forward port-forward-broken-pipe 8080:80 &
sleep 5 # wait for port-forward complete
./broke-my-pipe.py
