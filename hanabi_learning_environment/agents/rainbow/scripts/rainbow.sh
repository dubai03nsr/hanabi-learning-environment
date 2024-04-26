mkdir -p rainbow_results
python train.py --base_dir=results_base --mode=base &> rainbow_results/base.txt
python train.py --base_dir=results_cheat --mode=cheat &> rainbow_results/cheat.txt
python train.py --base_dir=tom0 --mode=tom0 &> rainbow_results/tom0.txt
python train.py --base_dir=tom1 --mode=tom1 &> rainbow_results/tom1.txt

python plot_returns.py