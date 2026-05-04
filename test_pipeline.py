from src.pipeline.run_pipeline import run_pipeline

def test_pipeline_runs():
    try:
        run_pipeline("AAPL")
        assert True
    except Exception:
        assert False