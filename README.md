# The Energy Measurement of AI Models Ontology
Modeling AI systems' characteristics of energy consumption and their sustainability level as an extension of the FAIR data principles has been considered only rudimentarily. In this work, we propose an **ontology for modeling the energy consumption and other environmental aspects of AI models**. The ontology can be used in various scenarios, ranging from an improved research data management to strategic controlling of institutions and the implementation of standards. 

Our ontology (OWL file) is available at **http://w3id.org/EMAI/ontology**

The ontology was evaluated based on the competency questions given below.

# Schema
![grafik](Green-AI-Ontology-Schema.png)

# Competency Questions
* Q1: In which region was the AI model trained? (Background: In a carbon-friendly region?)
* Q2: Did model A or model B consume more energy?
* Q3: Which energy measurement metric is most commonly used?
* Q4: What information related to energy consumption do researchers provide?
* Q5: Where was the ML Model trained?
* Q6: On what technical settings was the ML model trained?
* Q7: On which cloud provider was the ML model trained?
* Q8: How long has the ML model been trained?
* Q9: How much memory usage was required for the training?
* Q10: What is the average energy consumption of ML models developed and trained at the institution KIT?
* Q11: What metrics are there to indicate the power consumption of an AI model?
* Q12: How much kg of CO2eq did the Ai model generate?
* Q13: How much FPO (floating point operations) does the AI model need?

<!--- 
# Usage

```sparql
# get FPO
# CQ13
PREFIX emai: <https://w3id.org/EMAI/ontology>

SELECT * WHERE {
?AIModel a emai:AIModel .    
?AIModel emai:hasEnergyMetrics ?EnergyMetrics . 
?EnergyMetrics emai:hasFPO ?FloatingPointOperations . 
}
```
--->

# Related Work
The following papers have been considered for creating the ontology (ranked by decreasing citation count):

![grafik](https://user-images.githubusercontent.com/5419543/156885466-1be3b3c5-750d-4a91-9265-29e8c577d2e1.png)
