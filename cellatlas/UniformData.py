from seqspec.utils import load_spec
from seqspec.seqspec_find import find_by_region_id
from seqspec.utils import region_ids_in_spec
from seqspec.seqspec_index import run_index
from seqspec.seqspec_onlist import run_onlist
import os
from typing import List

MOD2FEATURE = {
    "TAG": "tags",
    "PROTEIN": "protein",
    "ATAC": "gDNA",
    "RNA": "cDNA",
    "CRISPR": "gRNA",
}


class UniformData:
    def __init__(
        self,
        seqspec_fn: str,
        modality: str,
        fastqs: List[str],
        fasta: str,
        gtf: str,
        feature_barcodes: str,
        output: str,
        all_feature_fastqs: List[List[str]] = [[]],
        x_string: str = "",
        onlist_fn: str = "",
    ) -> None:
        self.seqspec_fn = seqspec_fn
        self.seqspec = load_spec(seqspec_fn)
        self.modality = modality
        self.output = output
        self.all_fastqs = fastqs
        self.all_feature_fastqs = all_feature_fastqs

        # WIP start ----->
        # region_ids_in_spec(seqspec, modality, region_ids) is from seqspec.utils.py [LN:111]
        region_ids = [os.path.basename(i) for i in self.all_fastqs]
        print("\t\033[94m{}\033[0m\n".format(region_ids))
        # I believe it is looking for the fastq as a region_id, and is returning an empty list as a result.
        # That is no longer the specification. The fastq data is now recorded in a sequence_spec object:
        print("\n\033[94mget_seqspec:\033[0m\n{}".format(self.seqspec.get_seqspec(modality)))   
        # So will not appear in the regions (library_spec object):
        print("\n\033[94mget_libspec:\033[0m\n{}".format(self.seqspec.get_libspec(modality)))                
        # Below lines are from the function:
        spec = seqspec.get_libspec(modality)
        found = []
        for region_id in region_ids:
            found += [r.region_id for r in spec.get_region_by_id(region_id)]
            print("\t\033[94m{}\033[0m\n".format(region_id))
        # This needs to return some region(s) before we can proceed
        # <----- WIP end

        rids_in_spec = region_ids_in_spec(
            self.seqspec, self.modality, [os.path.basename(i) for i in self.all_fastqs]
        )
        self.spec_all_fastqs = [
            f for f in self.all_fastqs if os.path.basename(f) in rids_in_spec
        ]

        # filter the fastqs to feature fastqs (the type being feature associated with the modality)
        rgns = find_by_region_id(
            self.seqspec, self.modality, MOD2FEATURE.get(self.modality.upper(), "")
        )
        relevant_fqs = [rgn.parent_id for rgn in rgns]
        fqs = [f for f in self.all_fastqs if os.path.basename(f) in relevant_fqs]
        self.spec_feature_fastqs = fqs

        # note the use of rids_in_spec here, which is the same as the rids_in_spec above
        print("\n\033[94mrids_in_spec:\033[0m\n{}".format(rids_in_spec))
        self.x_string = run_index(self.seqspec_fn, self.modality, rids_in_spec, fmt="kb")

        self.fasta = fasta
        self.gtf = gtf
        self.feature_barcodes = feature_barcodes

        onlist = run_onlist(self.seqspec, self.modality, "barcode")
        # get onlist path relative to seqspec_fn path
        self.onlist_fn = os.path.join(os.path.dirname(self.seqspec_fn), onlist)
