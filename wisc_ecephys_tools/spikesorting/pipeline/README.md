# Spikesorting steps

1. Create a sorting script using (`run_sorting_template.py`)[template_scripts/run_sorting_template.py].
    - This may require populating certain YAML files in the `wisc_ecephys_tools/config` directory, likely including `sglx_sessions.yaml`, `sglx_experiments.yaml`, and `channels.yaml`.
2. Activate your spikesorting environment and run the script you created in step 1.
    - The branch of Kilosort you should be using (i.e. have checked out in git) is `CSC-UW/Kilosort/wisc/2.5/dev`. If in doubt, check this using `cd /Volumes/scratch/neuropixels/matlab/external/Kilosort-wisc-v2.5; git branch`.
    - This step will write CatGT (i.e. preprocessed) output to the `nvme` drive, and use that as input to Kilosort. The regular Kilosort output, and post-processed output, will then be written to the `nvme` drive for curation.
3. Check debugging plots generated by Kilosort, if applicable, to make sure that you don't need to re-run it (e.g. using branch `CSC-UW/Kilosort/wisc/2.5/non-rigid-template[-gda]`).
4. Curate the postprocessed output, ideally on the `nvme` array.
5. Create a script to compute quality metrics using (`run_quality_metrics_template.py`)[template_scripts/run_quality_metrics_template.py], and run it (still from within your spikesorting environment).
6. Open the results in `phy` and `File->Save`. This regenerates the `cluster_info.tsv` file with the metrics.
7. Move the final outputs (found in directories named `ks2_5_catgt_df_postpro_2_metrics_all_isi.imec*`) to `/Volumes/neuropixel_analysis`.
    - Example rysnc command: `cd /path/to/results; rsync -rvh --info=progress2 *metrics* /Volumes/neuropixel_analysis/destination_directory`
8. Remove all data (don't forget the CatGT output!) from the `nvme` array.