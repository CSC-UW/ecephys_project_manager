from .preprocessing import (
    run_preprocessing,
    CATGT_PROJECT_NAME,
    clear_catgt_output_files,
)
from .sorting import run_sorting
from .postprocessing import run_postprocessing


def run_pipeline(
    # paths and data
    project=None,
    prepro_project=CATGT_PROJECT_NAME,
    subject=None,
    experiment=None,
    alias=None,
    probe=None,
    # analysis names
    prepro_analysis_name=None,
    sorting_analysis_name=None,
    postpro_analysis_name=None,
    # misc
    clear_preprocessed_data=True,
    rerun_existing=False,
    dry_run=True,
):

    print(f"Running pipeline for {subject}, {probe}, {experiment}, {alias}")

    assert all(
        [
            arg is not None
            for arg in [
                project,
                subject,
                experiment,
                alias,
                probe,
                prepro_analysis_name,
                sorting_analysis_name,
                postpro_analysis_name,
            ]
        ]
    )
    if prepro_project is None:
        prepro_project = CATGT_PROJECT_NAME

    # Run CatGT
    print("\n\nRun preproecessing:")
    success = run_preprocessing(
        project=prepro_project,
        subject=subject,
        experiment=experiment,
        alias=alias,
        probe=probe,
        analysis_name=prepro_analysis_name,
        rerun_existing=rerun_existing,
        dry_run=dry_run,
    )
    if not dry_run and not success:
        return False

    # Run sorting
    print("\n\nRun sorting:")
    success = run_sorting(
        project=project,
        subject=subject,
        experiment=experiment,
        alias=alias,
        probe=probe,
        analysis_name=sorting_analysis_name,
        prepro_analysis_name=prepro_analysis_name,
        prepro_project=prepro_project,
        bad_channels=None,  # TODO
        rerun_existing=rerun_existing,
        dry_run=dry_run,
    )
    if clear_preprocessed_data:
        clear_catgt_output_files(
            project=prepro_project,
            subject=subject,
            experiment=experiment,
            alias=alias,
            probe=probe,
            analysis_name=prepro_analysis_name,
        )
    if not dry_run and not success:
        return False

    # Run postpro
    print("\n\nRun postprocessing:")
    success = run_postprocessing(
        project=project,
        subject=subject,
        experiment=experiment,
        alias=alias,
        probe=probe,
        analysis_name=postpro_analysis_name,
        sorting_name=sorting_analysis_name,
        rerun_existing=rerun_existing,
        dry_run=dry_run,
    )
    if not dry_run and not success:
        return False

    return True