# NERDz -- Named Entity Recognition for Algerian

This dataset is described in the paper ["*NERDz: A Preliminary Dataset of Named Entities for Algerian*"](https://aclanthology.org/2022.aacl-short.13/) by Samia Touileb, published in the Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing (Volume 2: Short Papers). 

In the NERDz dataset we added named entity annotations on top of the extension of the NArabizi treebank presented by [*Touileb and Barnes (2021)*](https://aclanthology.org/2021.findings-acl.324/), and which was originally introduced by [*Seddah et al. (2020)*](https://aclanthology.org/2020.acl-main.107/).

# The NArabizi treebank

The NArabizi ["*treebank*"](https://parsiti.github.io/NArabizi/) was developped by Seddah et al (2020). It contains manually annotated syntactic and morphological information,  and comprises around 1,500 sentences written in the Algerian dialect. These are mostly comments from newspapers' web forums (1,300 sentences from (Cotterell et al., 2014)),  in addition to 200 sentences from song lyrics.  The sentences are annotated on five different levels, covering tokenization, morphology, identification of code-switching, syntax, and translation to French (Seddah et al., 2020). Touileb and Barnes (2021) have further extended the NArabizi treebank, by first cleaning the treebank for duplicates, correcting some of the French translations, and some of the code-switching labels. But most importantly, they manually transliterated each sentence into purely arabic script and code-switched scripts. The treebank therefore has three parallel writing forms for each token in a sentence. They have also anotated each sentence of the treebank for sentiment and topic (see Touileb and Barnes (2021) for more details).  Due to the preprocessing, this version of the treebank (Touileb and Barnes, 2021) is a little bit smaller than the original treebank (Seddah et al., 2020).  See Table 1 in the ["*paper*"](https://aclanthology.org/2022.aacl-short.13/) to see an example of a NArabizi sentence transliterated to arabic and code-switched scripts. 

# The Named Entity annotations

The named entity annotations in NERDz are continuous, non-overlapping, spans of strings. The string boundaries follow the tokenization in the NArabizi treebank (Seddah et al., 2020),  where each token is assigned *one* entity type.  

The annotated files are distributed in two different formats:

- **conllu**: the original format of the treebank, where we added one additional column for the names entities. Here we used the tag "*name=*" to refer to the NER tag of each token.
- **bmes**: this format is added to facilitate the use of the data with NCRF++. These files are devided into the three different scripts of the treebank extended by Touileb and Barnes (2021). 

Both formats come in pre-defined train-dev-test splits, following the splits of the NArabizi treebank (Seddah et al. 2020).

# Entity types and definitions

NERDz is annotated using the IOB2 scheme for eight entity types: "PER", "GPE", "ORG", "NORP", "EVT", "LOC", "PROD", and "MISC". Our annotation guidelines are partly based on the ACE (Mitchell et al., 2003), ConLL (Tjong Kim Sang and De Meulder, 2003), and OntoNotes (Weischedel et al., 2013) datasets. Where each entity type is defined as follows:

- **PER**: all person names, including fictional characters.

- **GPE**: denotes mainly countries, but comprisesall entities with parliamentary-like governing systems. This means that states and cities are also GPEs.

- **ORG**: represent companies, organisations, and institutions. This includes political parties and football clubs. 

- **NORP**: refers to groups of people that share the same country (i.e., nationalities), same political beliefs, same religion, and proper nouns used to denote fans of football clubs. 

- **EVT**: this is similar to the OntoNotes (Weischedelet al., 2013) category, and includes all types of cultural, political, and sports events. In NERDz, this category is mainly related to sports events and political elections.

- **LOC**: all geographical places including continents, mountains, seas, buildings (e.g. football stadiums), streets, and neighborhoods.

- **PROD**: characterizes objects, or line of objects, aslong as they are produced by humans.e.g.,TVs and vehicles. 

- **MISC**: all entities that rarely occur in our dataset. These include quantities, money, diseases, and chemical components.

The table below shows the distribution of the annotated entities accross types and splits.

| Type | Train | Dev | Test | Total | %| 
| :--- | ---: | ---: | ---: | ---: | ---: |
| PER | 363 | 59 | 45 | 467 | 29.83 |
| GPE | 336 | 55 | 47 |438 | 27.97 |
| ORG | 237 | 22 | 31 | 290 | 18.52 |
| NORP | 183 | 29 | 23 | 235 | 15.00 |
| EVT | 45 | 5 | 4 | 54 | 3.45 |
| LOC | 33 | 3 | 5 | 41 | 2.62 |
| PROD | 14 | 7 | 2 | 23 | 1.46 |
| MISC | 18 | 0 | 0 | 18 | 1.15 | 
| Total | 1229 | 180 | 157| 1566| 100 |

# Manual annotations

Two  native  speakers  annotated  all  sentences from the NArabizi treebank. We compute two measures of agreement, *Krippendorff’s alpha* and *micro F1*-score. In terms of *Krippendorff’s alpha*, the agreement score is *α= 0.87*, which suggests strong evidence for good agreement.  The agreement in terms of *micro F1*-score achieved *86.3*. This evaluation score is based on SemEval 2013 task 9 evaluation scheme 3(Segura-Bedmar et al.,2013). Here, we used the strict measure, and compute F1 for exact match of both the entity boundary (the span of the entity), and the entity type. We disregard all annotations where both annotators agree that a token is not an entity, i.e., the "O" tag. 

# Cite

If you use or want to cite the dataset, or the results associated with our work, please cite the following paper:

```
@inproceedings{touileb-2022-nerdz,
    title = "{NERD}z: A Preliminary Dataset of Named Entities for {A}lgerian",
    author = "Touileb, Samia",
    booktitle = "Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 12th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)",
    month = nov,
    year = "2022",
    address = "Online only",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.aacl-short.13",
    pages = "95--101",
}
```
