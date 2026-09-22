#!/usr/bin/bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_ROOT}" || exit 1

buildDir="${1:-build}"

if ! [[ -d ${buildDir} ]]; then
  mkdir "${buildDir}" || exit
fi

mkdir -p "${buildDir}/sections" || exit
touch "${buildDir}/sections/0_abstract.aux"
touch "${buildDir}/sections/1_motivation.aux"
touch "${buildDir}/sections/2_fundamentals.aux"
touch "${buildDir}/sections/3_stateOfTheArt.aux"
touch "${buildDir}/sections/4_concept.aux"
touch "${buildDir}/sections/5_mathmetamodel.aux"
touch "${buildDir}/sections/6_digitalShadow.aux"
touch "${buildDir}/sections/7_evaluation.aux"
touch "${buildDir}/sections/8_futureWork.aux"
touch "${buildDir}/sections/9_acknowledgments.aux"
touch "${buildDir}/sections/10_appendix.aux"

latexmk -g -file-line-error -pdf -outdir="${buildDir}" main.tex || exit
makeindex "${buildDir}"/main.nlo -s nomencl.ist -o "${buildDir}"/main.nls || exit
latexmk -g -file-line-error -pdf -outdir="${buildDir}" main.tex || exit