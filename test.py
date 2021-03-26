import cobra.test
cobra_config = cobra.Configuration()
from cobra.test import create_test_model
model = create_test_model("textbook")
model.reactions.ACt2r