from pevolc.pipelines import train_forecaster

def test_training_pipeline_placeholder():
    assert callable(train_forecaster.run_training)
