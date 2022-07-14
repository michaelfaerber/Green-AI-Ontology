# The Energy Measurement of AI Models Ontology
Modeling AI systems' characteristics of energy consumption and their sustainability level as an extension of the FAIR data principles has been considered only rudimentarily. In this work, we propose an **ontology for modeling the energy consumption and other environmental aspects of AI models**. The ontology can be used in various scenarios, ranging from an improved research data management to strategic controlling of institutions and the implementation of standards. 

Our ontology (OWL file) is available at **http://w3id.org/EMAI/ontology**

The ontology was evaluated based on the competency questions given below.

You can use the following Microsoft Forms to provide your information about your AI model's energy consumption. This will successively increase our knowledge graph and add the data to the Linked Open Data Cloud: **https://forms.office.com/r/HYd4R9jutX**

[emai knowledge graph](emai-knowledge-graph)

# Schema
![grafik](emai-ontology-schema.png)

# Competency Questions
* Q1: How many floating-point operations (FPO) did the AI Model need to be trained?
* Q2: How much kg of CO2eq did the AI Model generate?
* Q3: How long did it take to train the AI Model?
* Q4: How much energy in kWh did the training of the AI model take?
* Q5: What Energy Measurement Services are used to calculate metrics about the AI Model's energy consumption?
* Q6: What energy metrics are used to indicate the energy consumption of an AI Model?
* Q7: How many times was the metric "floating-point operations" (FPO) used to indicate the energy consumption of AI models?
* Q8: What are the hardware settings used for training the AI Model?
* Q9: In which region is the hardware used to train the AI Model? (Background: In a carbon-friendly region?)
* Q10: How many GPUs were used to train the AI Model?
* Q11: Did AI Model A or AI Model B generate more CO2?
* Q12: Which programming language was used to train the AI Model?
* Q13: What software modules were used to train the AI Model?
* Q14: In the context of which research project was the AI Model developed?
* Q15: Which publication does the AI Model have?

# SPARQL Queries

Based on our created [EMAI Knowledge Graph](emai-knowledge-graph) we can answer all competency Questions listed above. In this section you can find the output of the SPARQL queries using our EMAI Knowledge Graph in GraphDB.

**[Query #1](emai-knowledge-graph):** Get the number of floating-point operations (FPO) that were needed to train the AI models.
Answers Competency Question Q1.
![grafik](sparql-queries/energy-metrics-fpo.png)

```sparql
# get several energy metrics that specify the energy consumption of an AI Model
# answers Q2, Q3 and Q4
```
![grafik](sparql-queries/energy-metrics-co2-runtime-kWh.png)

```sparql
# get infomations about which Energy Measurement Services are used
# answers Q5
```
![grafik](sparql-queries/energy-measurement-services.png)


```sparql
# get informations about which Energy Measurement Metrics are used
# answers Q6
```
![grafik](sparql-queries/energy-metrics.png)

```sparql
# get the total number how often the metric floating-point operations (FPO) is used
# answers Q7
```
![grafik](sparql-queries/total-number-fpo.png)

```sparql
# get several information about the hardware used to train an AI Model
# answers Q8, Q9 and Q10
PREFIX emai: <https://w3id.org/EMAI/>

SELECT * WHERE {
	?aiModel a emai:AIModel .
	?aiModel emai:hasHardwareSettings ?hardwareSettings .
	OPTIONAL {
	  	?hardwareSettings emai:hasHardwareType ?hardwareType .
		?hardwareSettings emai:hasMemory ?memory .
		?hardwareSettings emai:hasLocation ?location .
		?hardwareSettings emai:hasProvider ?provider .
	}
}
```

```sparql
# compare two AI Models
# answers Q11
```
![grafik](sparql-queries/compare-co2-two-models.png)

```sparql
# get several information about the software used to train an AI Model
# answers Q12 and Q13
PREFIX emai: <https://w3id.org/EMAI/>

SELECT * WHERE {
	?aiModel a emai:AIModel .
	?aiModel emai:hasSoftwareSettings ?softwareSettings .
	OPTIONAL {
		?softwareSettings emai:hasProgrammingLanguage ?programmingLanguage .
		?softwareSettings emai:hasModule ?module .
		?module emai:hasName ?moduleName .
	}
}
```

```sparql
# get several information about Publications and Research Projects related to the AI Models
# answers Q14 and Q15
PREFIX emai: <https://w3id.org/EMAI/>
PREFIX irao: <http://ontology.ethereal.cz/irao/>

SELECT * WHERE {
	?aiModel a emai:AIModel .
	?aiModel irao:hasPublication ?relatedPublication .
	?aiModel irao:hasResearchProject ?researchProject .
}

```
![grafik](sparql-queries/publication-project-info.png)

# Related Work
The following papers have been considered for creating the ontology (ranked by decreasing citation count):

![grafik](https://user-images.githubusercontent.com/5419543/156885466-1be3b3c5-750d-4a91-9265-29e8c577d2e1.png)
