if (!require("rmdformats", quietly = TRUE)) BiocManager::install("rmdformats")
rmarkdown::render("~/Documents/Repos/cellatlas/Hackathon.Rmd",
                  output_file = "~/Documents/Repos/cellatlas/Hackathon.html" )

