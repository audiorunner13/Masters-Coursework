---
  title: "EigenShoes - DATA605 Assignment 4"
author: "Peter Gatica"
date: "`r Sys.Date()`"
output: html_document
---

knitr::opts_chunk$set(echo = TRUE)

rm(list = ls())
library(jpeg)
library(OpenImageR)
library(Matrix)

# Initialization
# Set the file path directory of the jpg images
file_path <- "/Users/Audiorunner13/CUNY MSDS Course Work/DATA605 Fall 2022/Week 4/jpg"
shoe_test <- 4

#  Read and Plot the first image (.jpg)
img <- jpeg::readJPEG(paste0(file_path,"/RC_2500x1200_2014_us_53446.jpg"))

dim(img)

# Save the row,col,channels dimension
( row_dim <- dim(img)[1] )
( col_dim <- dim(img)[2] )
( channel_dim <- dim(img)[3] )

# plot the image
imageShow(img)

# Read in all image files
# Read to a list all filenames in folder

filenames <- list.files(path=file_path,pattern = ".jpg")

# Initialize the matrix where all files will be stored
all_images_data <- matrix(0, length(filenames), prod(dim(img)))

# Show the dimensions of the matrix
# Matrix is 17 x 9MM.  That is equals to 17 shoes, each having dimensions 1200 x 2500 x 3

dim(all_images_data)

# Function to Plot 1d Image Files

# This function didn't work in Markdown, it didn't display the image in the knitted file, so didn't use for submission.
# Does work correctly in RStudio

plot_shoe <- function(img1d) {
  img3d <- array(img1d,c(row_dim,col_dim,channel_dim))
  imageShow(img3d)
}

