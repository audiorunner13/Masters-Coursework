# title: "DATA608 - Module 3 Question 2 Shinyapp in R 
# Author - Peter Gatica"

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

# Calculate the national population in 2010

mort_stat_natl <- mort_stat %>%
  filter(Year == '2010' & ICD.Chapter == 'Neoplasms')

natl_pop_2010 <- sum(mort_stat_natl$Population)  # 308745538

# Sum the Total Deaths for each cause of death

natl_death_total_cod <- aggregate(mort_stat_2010$Deaths, by=list(mort_stat_2010$ICD.Chapter), FUN=sum)

# rename columns

names(natl_death_total_cod) <- c("ICD.Chapter", "Total_Deaths")

# Add total deaths nationally by cause of death

mort_stat_2010_new <- mort_stat_2010 %>% 
  right_join(natl_death_total_cod, by = "ICD.Chapter")

# Calculate and add the national mortality rate for each cause of death

(mort_stat_2010_new <- transform(mort_stat_2010_new, Natlional.Mortality.Rate = (Total_Deaths / natl_pop_2010)*100000))

# Question 2:
#   Often you are asked whether particular States are improving their mortality rates (per cause) faster than, or 
# slower than, the national average. Create a visualization that lets your clients see this for themselves for 
# one cause of death at the time. Keep in mind that the national average should be weighted by the national population.

shinyApp(
  ui = fluidPage(
    sidebarPanel(
      selectInput("icd.Chapter", "Cause of Death", mort_stat_2010_new[[1]])
    ),
    tableOutput("data")
  ),
  
  server = function(input, output) {
    
    output$data <- renderTable({
      ( df_out <- ((mort_stat_2010_new[, c("State", "Crude.Rate", "Natlional.Mortality.Rate"), drop = FALSE])[order(-mort_stat_2010_new$Crude.Rate),] %>% filter(mort_stat_2010_new == input$icd.Chapter) ) )
    }, rownames = TRUE)
    
  }
)
