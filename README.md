# The Energy Measurement of AI Models Ontology
Modeling AI systems' characteristics of energy consumption and their sustainability level as an extension of the FAIR data principles has been considered only rudimentarily. In this work, we propose an **ontology for modeling the energy consumption and other environmental aspects of AI models**. The ontology can be used in various scenarios, ranging from an improved research data management to strategic controlling of institutions and the implementation of standards. 

Our ontology (OWL file) is available at **http://w3id.org/EMAI/ontology**

The ontology was evaluated based on the competency questions given below.

# Schema
![grafik](Green-AI-Ontology-Schema.png)

# Competency Questions
* Q1: How many floating-point operations (FPO) did the AI Model need to be trained?
* Q2: How much kg of CO2eq did the AI Model generate?
* Q3: How long did it take to train the AI model?
* Q4: What is the social cost in US$ that the AI model has generated?
* Q5: What Energy Measurement Services are used to calculate metrics about the AI Model's energy consumption?
* Q6: What energy metrics are used to indicate the energy consumption of an AI Model?
* Q7: How many times was the metric "floating-point operations" (FPO) used to indicate the energy consumption of AI models?
* Q8: What are the hardware settings used for training the AI Model?
* Q9: In which region is the hardware used to train the AI model? (Background: In a carbon-friendly region?)
* Q10: Which provider (cloud service) was used to train the AI Model?
* Q11: Did AI Model A or AI Model B consume more energy?
* Q12: Which programming language was used to train the AI Model?
* Q13: What software modules were used to train the AI Model?
* Q14: In the context of which research project was the AI Model developed?
* Q15: Which publication does the AI Model have?

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
