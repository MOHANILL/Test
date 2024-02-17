#session 9-2
from    tkinter import *
window=Tk()
window.title("scrollbar")
window.geometry("700x7000+500+250")
text=Text(window,heigh=20, width=30)
text.pack()
scroll=Scrollbar(window)

text.pack(side=LEFT,fill=Y)
scroll.pack(side=RIGHT,fill=Y)

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
par="""   Generating long and coherent text is an important but challenging task, particularly for open-ended language generation tasks such as story generation. Despite the success in modeling intra-sentence coherence, existing generation models (e.g., BART) still struggle to maintain a coherent event sequence throughout the generated text. We conjecture that this is because of the difficulty for the decoder to capture the high-level semantics and discourse structures in the context beyond token-level co-occurrence. In this paper, we propose a long text generation model, which can represent the prefix sentences at sentence level and discourse level in the decoding process. To this end, we propose two pretraining objectives to learn the representations by predicting inter-sentence semantic similarity and distinguishing between normal and shuffled sentence orders. Extensive experiments show that our model can generate more coherent texts than state-of-the-art baselines. 

Comments: 	ACL 2021 Long Paper
Subjects: 	Computation and Language (cs.CL)
Cite as: 	arXiv:2105.08963 [cs.CL]
  	(or arXiv:2105.08963v1 [cs.CL] for this version)
  	
https://doi.org/10.48550/arXiv.2105.08963
Submission history
From: Jian Guan [view email]
[v1] Wed, 19 May 2021 07:29:08 UTC (5,674 KB)
Download:

    PDF
    Other formats

(license)
Current browse context:
cs.CL
< prev   |   next >
new | recent | 2105
Change to browse by:
cs
References & Citations

    NASA ADS
    Google Scholar
    Semantic Scholar

DBLP - CS Bibliography
listing | bibtex
Jian Guan
Changjie Fan
Zitao Liu"""

text.insert(END,par)
window.mainloop()