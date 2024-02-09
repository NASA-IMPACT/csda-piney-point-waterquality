# Load necessary library
library(ggplot2)
library(dplyr)
library(tidyr)
library(keras)

# Data preparation 
Filtered_Data_AllStations <- read.csv("~/Downloads/Filtered_Data_AllStations.csv")
data <- data.frame(Filtered_Data_AllStations[c(9,12)])

# Split the data into training and testing sets (e.g., 80% for training, 20% for testing)
set.seed(123)
sample_indices <- sample(1:nrow(data), 0.8 * nrow(data))
train_data <- data[sample_indices, ]
test_data <- data[-sample_indices, ]


model <- keras_model_sequential() %>%
  layer_dense(units = 64, activation = "relu", input_shape = 1) %>%
  layer_dense(units = 1)  # Output layer with one neuron (for regression)

model %>% compile(
  loss = "mean_squared_error",
  optimizer = optimizer_adam(),  # You can choose different optimizers
  metrics = c("mean_squared_error")
)

history <- model %>% fit(
  x = as.matrix(train_data$satelliteval),
  y = train_data$Original_R,
  epochs = 200,  # Number of training iterations
  verbose = 1
)

evaluation <- model %>% evaluate(
  x = as.matrix(test_data$satelliteval),
  y = test_data$Original_R
)

cat("Mean Squared Error (MSE):", evaluation[["mean_squared_error"]], "\n")

predictions <- model %>% predict(as.matrix(test_data$satelliteval))

# Get the model summary to see the architecture and the number of parameters
summary(model)

# Extract weights and biases
weights <- get_weights(model)
intercept <- weights[[1]][1]  # This is the intercept (bias)
slope <- weights[[2]][1]      # This is the slope (weight)

# Print the regression equation
cat("Regression Equation: y =", slope, "* x +", intercept, "\n")


