## Title: Description of a business Problem

> "Don’t try to solve a problem that doesn’t exist." - Me

### Business Area: Healthcare :hospital:

### The Business Problem:

The time of exam's lifecycle spent between PHC and SHC is too high. 

### Who are the Stakeholders? What are their roles?

- Laboratory Owners/Managers: Aim for more productivity and communication between patients and hospital to dispatch their results as soon as possible.

- Hospital Doctors: Make the first apointment with the patient(Primary health care) and redirect them to do the exam at the laboratories(secondary health care) and, after receiving the results, give them to the patients and follow the procedure accordingly.

- Patient: Come to the hospital, make the apointment, go to the labolatories and do the exam, then wait for the results to arrive again to the hospital to receive the feedback from the doctor.

### In which process is the problem related to? What is the background?

The problem is related to the pipeline of the exams required after taken the first apointment. In other words, the journey between the Primary and the Secondary care phases.

#### Background:

- The exam, once getting it's results, has to assigned and be tranported to the hospital fisically within the time limited by law.
- Hundreds of exams to dispatch
- The time taken for the exam to arrive at the doctor's hand is crucial for early treatment for some diseases.
- Some patients don't go to the doctor's office to get the results of the exam due to geographical issues.

### What are the relevant data to understand the problem? Is it available?

There are three insights that we need to have in order to understand the problem. First, the records of the exams, which can be retrieved from [*e-SUS APS - Secretaria de Atenção Primária à Saúde*](https://sisaps.saude.gov.br/esus/), for example. Secondly, we need to know whether the exam is ready to be assigned by the laborary or not, that information is available, for example, in the SIS "something" systems, for example, in the [*Sistema de Informação do Câncer (SISCAN)*](http://w3.datasus.gov.br/siscam/index.php). And last but not least, we(our application) need to be connected to the  [*Rede Nacional de Dados em Saúde (RNDS)*](https://datasus.saude.gov.br/rnds-2/) in order to receive that data. (in conformity with the [*FHIR*](https://hl7.org/FHIR/) specification of course ;)).

github: [PAVincius](https://github.com/PAVincius/I2A2_2022)