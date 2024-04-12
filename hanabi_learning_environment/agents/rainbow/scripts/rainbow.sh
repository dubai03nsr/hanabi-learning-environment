for tom_lambda in 0 1e-5 1e-4 1e-3 1e-2 1e-1 1
do
        python train.py --base_dir=results --tom_lambda=$tom_lambda > rainbow_results/$tom_lambda.txt 2>&1
done
