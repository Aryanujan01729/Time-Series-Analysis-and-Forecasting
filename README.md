# Time-Series-Analysis-and-Forecasting
Autoregressive Integrated Moving Average (ARIMA):
Situations: Suitable for univariate time series data with a clear trend and seasonality.
Criteria: When the data exhibits a stationary behavior after differencing.

Seasonal-Trend decomposition using LOESS (STL):
Situations: Useful when the time series data has a strong seasonality and a clear trend.
Criteria: When you need to decompose the time series into trend, seasonal, and remainder components.

Exponential Smoothing State Space Models (ETS):
Situations: Appropriate for time series with exponential trends and/or seasonality.
Criteria: When you want a simple and flexible model that can adapt to different types of time series patterns.

Prophet:
Situations: Ideal for time series with daily observations and strong seasonal patterns.
Criteria: When you have missing data points and outliers, and need a model that can handle these situations robustly.

Long Short-Term Memory (LSTM) Networks:
Situations: Suitable for complex time series with long-term dependencies and nonlinear patterns.
Criteria: When dealing with large datasets and the need to capture complex temporal relationships.

Gated Recurrent Unit (GRU) Networks:
Situations: Similar to LSTM, GRU is useful for capturing long-term dependencies in time series data.
Criteria: When a more computationally efficient model is required compared to LSTM.

ARIMA with Exogenous Variables (ARIMAX):
Situations: When external factors (exogenous variables) impact the time series and need to be considered in the model.
Criteria: When there are known predictors that influence the time series.

Vector Autoregression (VAR):
Situations: Suitable for multivariate time series where multiple variables influence each other.
Criteria: When the relationships between different time series variables are of interest.

Facebook's NeuralProphet:
Situations: Designed for forecasting with daily data that may contain missing values.
Criteria: When you need a model that combines elements of classical time series methods with neural network architectures.

Theta Method:
Situations: Suitable for time series with a constant trend and no seasonality.
Criteria: When a simple and computationally efficient method is sufficient for forecasting.
