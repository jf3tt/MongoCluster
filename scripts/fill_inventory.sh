#!/bin/bash

info=$(sudo docker inspect -f '{{.Name}} {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps -q))

for x in "$info" 
do
				echo "[local]" > ../inventory.new
				echo "[127.0.0.1]" >> ../inventory.new
				echo "[nodes]" >> ../inventory.new
				echo "$x" | grep node | awk '{print $2}' >> ../inventory.new

				echo "[mongos]" >> ../inventory.new
				echo "$x" | grep mongos | awk '{print $2}' >> ../inventory.new

				echo "[config]" >> ../inventory.new
				echo "$x" | grep config | awk '{print $2}' >> ../inventory.new
done
