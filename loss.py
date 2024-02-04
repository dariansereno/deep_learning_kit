from abc import ABC, abstractmethod
import numpy as np

class Loss(ABC):
	@abstractmethod
	def forward(self):
		pass

	def calculate(self, output, y):
		sample_losses = self.forward(output, y)
		data_loss = np.mean(sample_losses)
		return data_loss

class Loss_CategoricalCrossEntropy(Loss):
	def forward(self, y_pred, y_true):
		samples = len(y_pred)
		y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

		#print(y_true)
		if len(y_true.shape) == 1:
			correct_confidences = y_pred_clipped[range(samples), y_true]
		elif len(y_true.shape) == 2:
			correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
		
		negative_log_likelihoods = np.log(correct_confidences)
		return negative_log_likelihoods