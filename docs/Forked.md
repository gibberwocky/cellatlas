
## Initiate conda environment ##

```bash
# Create conda environment
mamba create --name cellatlas python=3.12.7
mamba activate cellatlas
```

## Install dependencies ##

```bash
cd ~/software

# Install `tree` to view files
git clone https://github.com/adsr/tree.git
cd tree
# If on OSX make sure to edit Makefile
make -j16 && make install
# This does return errors, but the tool in bin appears to work

# Install `jq, a command-line tool for extracting key value pairs from JSON files 
git clone https://github.com/jqlang/jq.git
git submodule update --init
autoreconf -i
./configure --with-oniguruma=builtin
make clean
make -j8
make check
sudo make install

# Install git pip
mamba install git pip

# Install gget (https://github.com/pachterlab/gget) for efficientey querying of genomic dbs
pip install --upgrade gget

# Install kb-python (https://github.com/pachterlab/kb_python) wrapper for kallisto and bustools
pip install --upgrade kb-python

```

## Install cellatlas (forked) and seqspec

```bash
# Install cellatlas (from repo)
#pip install --quiet git+https://github.com/cellatlas/cellatlas.git
pip install git+https://github.com/gibberwocky/cellatlas.git --force-reinstall

# Install seqspec
pip install --quiet git+https://github.com/pachterlab/seqspec.git
```

# RNA split-seq example

```bash
mv /examples/rna-splitseq ../cellatlas-examples && cd ../cellatlas-examples
gunzip barcode*
seqspec print spec.yaml
```

Note that the above returns an error because `~/cellatlas-example/spec.yaml` is based on an earlier version of specseq. More assay templates are available at [https://www.sina.bio/seqspec-builder/assays.html](https://www.sina.bio/seqspec-builder/assays.html). Here I have copied the WT-Mega-v2 spec.

Get reference genome fasta and gtf annotation links as a JSON file, extract and download the respective files.

```bash
gget ref -o ref.json -w dna,gtf mus_musculus
curl -LO $(jq -r '.mus_musculus.genome_dna.ftp' ref.json)
curl -LO $(jq -r '.mus_musculus.annotation_gtf.ftp' ref.json)
```

Run cellatlas:

```bash
cellatlas build -o out -m rna -s WT-Mega-v2.yaml \
  -fa Mus_musculus.GRCm39.dna.primary_assembly.fa.gz \
  -g Mus_musculus.GRCm39.113.gtf.gz \
  fastqs/R1.fastq.gz fastqs/R2.fastq.gz
```

Current issue:

```bash
Traceback (most recent call last):
  File "/Users/s14dw4/miniforge3/envs/cellatlas/bin/cellatlas", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/Users/s14dw4/miniforge3/envs/cellatlas/lib/python3.12/site-packages/cellatlas/main.py", line 45, in main
    COMMAND_TO_FUNCTION[sys.argv[1]](parser, args)
  File "/Users/s14dw4/miniforge3/envs/cellatlas/lib/python3.12/site-packages/cellatlas/cellatlas_build.py", line 97, in validate_build_args
    UniformData(
  File "/Users/s14dw4/miniforge3/envs/cellatlas/lib/python3.12/site-packages/cellatlas/UniformData.py", line 46, in __init__
    rgns = run_find_by_type(
           ^^^^^^^^^^^^^^^^
NameError: name 'run_find_by_type' is not defined
```