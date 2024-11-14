# Objective

Update [cellatlas](https://github.com/cellatlas/cellatlas)(v.0.0.0) to work with the latest release of [seqspec](https://github.com/pachterlab/seqspec)(v.0.3.1). The current release of [cellatlas] works with an in-between release of [seqspec] which appears to be based on the [seqspec] v.0.2.0 specification.

## seqspec specification

* [v0.1.1](seqspec-specifications/v0.1.1/SPECIFICATION.md)
* [v0.2.0](seqspec-specifications/v0.2.0/SPECIFICATION.md)
* [v0.3.1](seqspec-specifications/v0.3.1/SPECIFICATION.md)

## seqspec source

* [v0.1.1](https://github.com/gibberwocky/cellatlas/tree/main/seqspec-source/v0.1.1/seqspec)
* [v0.2.0](https://github.com/gibberwocky/cellatlas/tree/main/seqspec-source/v0.2.0/seqspec)
* [v0.3.1](https://github.com/gibberwocky/cellatlas/tree/main/seqspec-source/v0.3.1/seqspec)

## Maxwell setup

To install the `cellatlas` fork and latest `seqspec`:

```bash
# Create conda environment
module load mamba
mamba create --name cellatlas_fork python=3.7
mamba activate cellatlas_fork
mamba install gget
mamba install kb-python
mamba install git pip
# Install cellatlas fork
pip install git+https://github.com/gibberwocky/cellatlas.git
# Install latest seqspec release
pip install git+https://github.com/pachterlab/seqspec.git
```

### Functional cellatlas + seqspec

To install a functional version of `cellatlas` and `seqspec` (i.e. the in-between release):

For reference, the
```bash
# Create conda environment
module load mamba
mamba create --name cellatlas python=3.7
mamba activate cellatlas
mamba install gget
mamba install kb-python
mamba install git pip
# Install cellatlas
pip install git+https://github.com/cellatlas/cellatlas.git
# Install in-between seqspec release
pip install git+https://github.com/pachterlab/seqspec.git@9471a317f524c289ee6582c1889cdeac0c5396b2
```
