# title: "DATA608 - Module 1 R Notebook, Author - Peter Gatica"

# load libraries
library(shiny)
library(tidyverse)
library(tidytext)
library(ggplot2)
library(gcookbook)
library(dplyr)
library(knitr)
library(RCurl)

# retrieve CDC data

filename <- getURL("https://raw.githubusercontent.com/charleyferrari/CUNY_DATA608/master/lecture3/data/cleaned-cdc-mortality-1999-2010-2.csv")

mort_stat <- read.csv(text=filename, header=TRUE)

# Filter Year 2010 Data

mort_stat_2010 <- mort_stat %>%
  filter(Year == '2010')

# Question 1:
#   As a researcher, you frequently compare mortality rates from particular causes across different States. You need a 
# visualization that will let you see (for 2010 only) the crude mortality rate, across all States, from one cause 
# (for example, Neoplasms, which are effectively cancers). Create a visualization that allows you to rank States by 
# crude mortality for each cause of death. 

shinyApp(
  ui = fluidPage(
    sidebarPanel(
      selectInput("icd.Chapter", "Cause of Death", mort_stat_2010[[1]])
    ),
    tableOutput("data")
  ),
  
  server = function(input, output) {
    
    output$data <- renderTable({
      ( df_out <- ((mort_stat_2010[, c("State", "Crude.Rate"), drop = FALSE])[order(-mort_stat_2010$Crude.Rate),]  %>% 
                     filter(mort_stat_2010 == input$icd.Chapter)) )
      }, rownames = TRUE)
    
  }
)