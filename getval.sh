#!/bin/sh
FILE=res.csv

if [ -f "$FILE" ]; then
    rm "$FILE"
fi

for i in 1 2 3 4 5 6
do
    A=`./build/diffusion_fem meshes/unit_square${i}.vtk | awk 'NF>1{print $NF}'`
    echo -n "${A##* }" | tr '\n' ',' >> "$FILE"
    echo >> "$FILE"
done
