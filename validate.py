from dump_LUTS import DumpParser
from lut_pkg import PkgParser
from utils import log

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dump", required=True)
parser.add_argument("--pkg", required=True)
args = parser.parse_args()

with open(args.dump) as f:
    parser = DumpParser()
    dump_luts = parser.parse(f)
    for lut in dump_luts:
        log("found dump_lut, name:", lut.name, "size:", len(lut.data))

with open(args.pkg) as f:
    parser = PkgParser()
    pkg_luts = parser.parse(f)
    for lut in pkg_luts:
        log("found pkg_lut, name:", lut.name, "size:", len(lut.data))

log("----")
log("reverse matching VHDL LUTs onto emulator LUTs...")
log("----")

for dump_lut in dump_luts:
    log(dump_lut.name)
    matches = []
    for pkg_lut in pkg_luts:
        if pkg_lut.data == dump_lut.data:
            matches.append(pkg_lut)
    if matches:
        for pkg_lut in matches:
            log("  matches", pkg_lut.name, color='green')
    else:
        log("  *** NO matches", color='red')
    log("----")

log("matching by mapping...")
log("----")

mapping = (
    ("Cal-Mu Eta EG-MU", "CALO_ETA_CONV_2_MUON_ETA_LUT"),
    ("Cal-Mu Eta JET-MU", "CALO_ETA_CONV_2_MUON_ETA_LUT"),
    ("Cal-Mu Eta TAU-MU", "CALO_ETA_CONV_2_MUON_ETA_LUT"),
    ("Cal-Mu Phi EG-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),
    ("Cal-Mu Phi ETM-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),
    ("Cal-Mu Phi ETMHF-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),
    ("Cal-Mu Phi HTM-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),
    ("Cal-Mu Phi JET-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),
    ("Cal-Mu Phi TAU-MU", "CALO_PHI_CONV_2_MUON_PHI_LUT"),

    ("Delta Eta EG-EG", "CALO_CALO_DIFF_ETA_LUT"),
    ("Delta Eta EG-JET", "CALO_CALO_DIFF_ETA_LUT"),
    ("Delta Eta EG-MU", "CALO_MU_DIFF_ETA_LUT"),
    ("Delta Eta EG-TAU", "CALO_CALO_DIFF_ETA_LUT"),
    ("Delta Eta JET-JET", "CALO_CALO_DIFF_ETA_LUT"),
    ("Delta Eta JET-MU", "CALO_MU_DIFF_ETA_LUT"),
    ("Delta Eta JET-TAU", "CALO_CALO_DIFF_ETA_LUT"),
    ("Delta Eta MU-MU", "MU_MU_DIFF_ETA_LUT"),
    ("Delta Eta TAU-MU", "CALO_MU_DIFF_ETA_LUT"),
    ("Delta Eta TAU-TAU", "CALO_CALO_DIFF_ETA_LUT"),

    ("Delta Phi EG-EG", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi EG-ETM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi EG-ETMHF", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi EG-HTM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi EG-JET", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi EG-MU", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi EG-TAU", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi JET-ETM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi JET-ETMHF", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi JET-HTM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi JET-JET", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi JET-MU", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi JET-TAU", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi MU-ETM", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi MU-ETMHF", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi MU-HTM", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi MU-MU", "MU_MU_DIFF_PHI_LUT"),
    ("Delta Phi TAU-ETM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi TAU-ETMHF", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi TAU-HTM", "CALO_CALO_DIFF_PHI_LUT"),
    ("Delta Phi TAU-MU", "CALO_MU_DIFF_PHI_LUT"),
    ("Delta Phi TAU-TAU", "CALO_CALO_DIFF_PHI_LUT"),

    ("Cosh EG-EG", "CALO_CALO_COSH_DETA_LUT"),
    ("Cosh EG-JET", "CALO_CALO_COSH_DETA_LUT"),
    ("Cosh EG-MU", "CALO_MUON_COSH_DETA_LUT"),
    ("Cosh EG-TAU", "CALO_CALO_COSH_DETA_LUT"),
    ("Cosh JET-JET", "CALO_CALO_COSH_DETA_LUT"),
    ("Cosh JET-MU", "CALO_MUON_COSH_DETA_LUT"),
    ("Cosh JET-TAU", "CALO_CALO_COSH_DETA_LUT"),
    ("Cosh MU-MU", "MU_MU_COSH_DETA_LUT"),
    ("Cosh TAU-MU", "CALO_MUON_COSH_DETA_LUT"),
    ("Cosh TAU-TAU", "CALO_CALO_COSH_DETA_LUT"),

    ("Cos EG", "CALO_COS_PHI_LUT"),
    ("Cos EG-EG", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos EG-ETM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos EG-ETMHF", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos EG-HTM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos EG-JET", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos EG-MU", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos EG-TAU", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos JET", "CALO_COS_PHI_LUT"),
    ("Cos JET-ETM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos JET-ETMHF", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos JET-HTM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos JET-JET", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos JET-MU", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos JET-TAU", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos MU", "MUON_COS_PHI_LUT"),
    ("Cos MU-ETM", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos MU-ETMHF", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos MU-HTM", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos MU-MU", "MU_MU_COS_DPHI_LUT"),
    ("Cos TAU", "CALO_COS_PHI_LUT"),
    ("Cos TAU-ETM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos TAU-ETMHF", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos TAU-HTM", "CALO_CALO_COS_DPHI_LUT"),
    ("Cos TAU-MU", "CALO_MUON_COS_DPHI_LUT"),
    ("Cos TAU-TAU", "CALO_CALO_COS_DPHI_LUT"),

    ("Sin EG", "CALO_SIN_PHI_LUT"),
    ("Sin JET", "CALO_SIN_PHI_LUT"),
    ("Sin MU", "MUON_SIN_PHI_LUT"),
    ("Sin TAU", "CALO_SIN_PHI_LUT"),

    ("Pt Mass_EG-ET", "EG_PT_LUT"),
    ("Pt Mass_ETM-ET", "EG_PT_LUT"),
    ("Pt Mass_ETMHF-ET", "EG_PT_LUT"),
    ("Pt Mass_HTM-ET", "EG_PT_LUT"),
    ("Pt Mass_JET-ET", "JET_PT_LUT"),
    ("Pt Mass_MU-ET", "MU_PT_LUT"),
    ("Pt Mass_TAU-ET", "EG_PT_LUT"),

    ("Pt TwoBody_EG-ET", "EG_PT_LUT"),
    ("Pt TwoBody_ETM-ET", "EG_PT_LUT"),
    ("Pt TwoBody_ETMHF-ET", "EG_PT_LUT"),
    ("Pt TwoBody_HTM-ET", "EG_PT_LUT"),
    ("Pt TwoBody_JET-ET", "JET_PT_LUT"),
    ("Pt TwoBody_MU-ET", "MU_PT_LUT"),
    ("Pt TwoBody_TAU-ET", "EG_PT_LUT"),
)
for dump_name, pkg_name in mapping:
    log()
    log(dump_name, "<-->", pkg_name)
    dump_lut = list(filter(lambda lut: lut.name == dump_name, dump_luts))[0]
    pkg_lut = list(filter(lambda lut: lut.name == pkg_name, pkg_luts))[0]
    if dump_lut.data == pkg_lut.data:
        log("  size:", len(dump_lut.data))
        log("  FULL_MATCH", color='green')
    else:
        dump_len = len(dump_lut.data)
        pkg_len = len(pkg_lut.data)
        if dump_len != pkg_len:
            log("  *** SIZE_MISMATCH dump={} vs pkg={}".format(dump_len, pkg_len), color='red')
        else:
            errors = []
            for i in range(dump_len):
                if dump_lut.data[i] != pkg_lut.data[i]:
                    errors.append((dump_lut.data[i], pkg_lut.data[i]))
            log("  *** {} DATA_MISMATCHES of {}".format(len(errors), dump_len), color='red')
        begin = ", ".join([str(value) for value in dump_lut.data[:8]])
        end = ", ".join([str(value) for value in dump_lut.data[-8:]])
        log("  dump: [{} ... {}]".format(begin, end))
        begin = ", ".join([str(value) for value in pkg_lut.data[:8]])
        end = ", ".join([str(value) for value in pkg_lut.data[-8:]])
        log("  pkg:  [{} ... {}]".format(begin, end))

