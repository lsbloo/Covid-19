## DBPerformace
   <p> 
       Ferramenta para análise de desempenho de banco de dados. 
   </p>
* Using generator_data.py

## Table of content
- [Getting Started]
- [Requirements](
- [How to Build]
- [How to Run]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements

For building and running the application you need:

- Localize requeriments.txt 
- apply this comand pip3 install -r requeriments.txt

#### Environment Variables

- DATABASE_NAME=covid19
- DATABASE_HOST=localhost
- DATABASE_USER=postgres
- DATABASE_PASSWORD=admin
- DATABASE_PORT=5434
- PATH_CSV=/home/osvaldoairon/Dev/coronavirus-csv
- NAME_CSV=coronavirus_dataset.csv
- URL_MONGO_DB=mongodb://localhost:27017/



### How to Run

  * Help
         -> python3 generator_data.py --help
  
  ### Performace Graph
  
  <br>
  
  ![Screenshot](insert_01.png 'Performace Inserção')
  
  <br>
  <br>
  <br>
  
  ![Screenshot](recovery_1.png 'Performace Leitura')
