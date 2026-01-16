# prompts have the following structure: 
# for each competence, the first prompt is about providing verbal explanation (number + explanation),
# the second prompt is about numerical annotation only.

# Define general instructions for competence annotation

promptAD = {
    # --- Probleemanalyse (Problem analysis) ---
    "AD_PROBL": (
        "AD_PROBL",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses in an asynchronous 
video role-playing exercise. In this role-playing exercise, the candidate responds verbally to a fictional business owner 
named Charina, across three scenes. Charina shares a strategic dilemma about expanding her sustainable retail business online, 
describes conflicts within her management team, and asks the candidate for advice and direct support. More specifically:

- **Scene 1**: Charina explains the company's history—from 1 to 12 stores in 10 years, founded on strong principles 
of sustainability and fair trade. She reveals the core conflict: a debate within the management team (MT) about launching 
an online sales channel. She outlines three opposing options (full launch, no launch, small-scale pilot) and asks, 
"How do you take a good decision here?"
- **Scene 2**: Charina admits she loses sleep over the decision. She is torn between the impersonal nature of online sales 
and the potential exposure, and is worried about the impact on loyal staff. She then makes a direct request: 
"Can you perhaps chair our next MT meeting? So we can finally reach a decision together?"
- **Scene 3**: Charina acknowledges the candidate's input but states she is still not decided and finds it difficult. 
She presses for concrete next steps: "What do you mainly advise me? And what can you do for me? What should I tackle first, do you think?"
- **Scene 4**: Scene 4 is the final wrap-up instruction to the candidate, summarizing and closing the conversation.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

        **Competency to evaluate:**  
**Problem Analysis** - The candidate's ability to dissect the complex, multi-faceted situation 
presented by Charina to identify the core issues, their interconnections, and their relative importance.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The response is generic, avoids the problem, or focuses on irrelevant side issues. 
The candidate fails to distinguish between main and side issues, does not make connections, 
and does not identify the core problem.
- **2** (Fair): The candidate identifies surface-level issues but treats them in isolation. 
The response may list problems without prioritizing them or making meaningful connections. 
The core of the issue is only partially or incorrectly identified.
- **3** (Satisfactory): The candidate identifies the main issues and begins to connect them. 
They may distinguish main from side issues but not with high clarity. 
The core problem is identified at a basic level.
- **4** (Good): The candidate clearly distinguishes main issues from side issues and actively explores 
the connections between them. They identify a more nuanced core problem.
- **5** (Excellent): The candidate demonstrates a sophisticated, holistic understanding. 
They seamlessly integrate all aspects of the problem and identify the deep, systemic core issue. 
Their analysis reveals non-obvious connections and gets to the fundamental root cause.


**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Problem Analysis" competency.
- Map the candidate's performance to the rubric above.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

Transcript:
```{text}```
"""
    ),

    # --- Creativiteit (Creativity) ---
    "AD_CREAT": (
        "AD_CREAT",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses in an asynchronous 
video role-playing exercise. In this role-playing exercise, the candidate responds verbally to a fictional business owner 
named Charina, across three scenes. Charina shares a strategic dilemma about expanding her sustainable retail business online, 
describes conflicts within her management team, and asks the candidate for advice and direct support. More specifically:

- **Scene 1**: Charina explains the company's history—from 1 to 12 stores in 10 years, founded on strong principles 
of sustainability and fair trade. She reveals the core conflict: a debate within the management team (MT) about launching 
an online sales channel. She outlines three opposing options (full launch, no launch, small-scale pilot) and asks, 
"How do you take a good decision here?"
- **Scene 2**: Charina admits she loses sleep over the decision. She is torn between the impersonal nature of online sales 
and the potential exposure, and is worried about the impact on loyal staff. She then makes a direct request: 
"Can you perhaps chair our next MT meeting? So we can finally reach a decision together?"
- **Scene 3**: Charina acknowledges the candidate's input but states she is still not decided and finds it difficult. 
She presses for concrete next steps: "What do you mainly advise me? And what can you do for me? What should I tackle first, do you think?"
- **Scene 4**: Scene 4 is the final wrap-up instruction to the candidate, summarizing and closing the conversation.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

        **Competency to evaluate:**  
**Creativity** - The candidate's ability to generate novel, diverse, and well-integrated ideas 
in response to Charina's complex, multi-faceted problems.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The candidate shows no creativity. Their response is generic, repetitive, 
or avoids generating any concrete ideas. They stick to clichés and do not approach the problem 
from new angles or combine information in a novel way.
- **2** (Fair): The candidate suggests one or two basic, conventional ideas. They may acknowledge 
different perspectives but do not explore them deeply or use them to generate solutions. 
Their ideas are simple combinations of existing elements without significant novelty.
- **3** (Satisfactory): The candidate generates a few relevant ideas that go beyond the obvious. 
They attempt to view the problem from more than one perspective and combine different aspects 
of Charina's story to form a coherent, if not highly original, suggestion.
- **4** (Good): The candidate produces multiple, original ideas that are clearly tailored to the nuances 
of Charina's situation. They actively synthesize different perspectives (e.g., financial, personal, 
team dynamics, brand values) to create innovative solutions. Their approach demonstrates flexibility and novel thought.
- **5** (Excellent): The candidate demonstrates exceptional creativity by generating insightful, 
non-obvious, and highly sophisticated ideas. They seamlessly integrate all facets of the problem 
(e.g., personal, strategic, operational) to propose novel pathways or frameworks. Their suggestions 
often reveal a deep, systemic understanding and introduce entirely new, viable possibilities 
that were not initially apparent.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Creativity" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant proposes a structured, creative process (e.g., a specific type of brainstorm or scenario workshop) 
to unlock new ideas with the team, showing how to generate creativity in others.

Transcript:
```{text}```
"""
    ),

    # --- Oordeelsvorming (Judgment Formation) ---
    "AD_OORDE": (
        "AD_OORDE",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses in an asynchronous 
video role-playing exercise. In this role-playing exercise, the candidate responds verbally to a fictional business owner 
named Charina, across three scenes. Charina shares a strategic dilemma about expanding her sustainable retail business online, 
describes conflicts within her management team, and asks the candidate for advice and direct support. More specifically:

- **Scene 1**: Charina explains the company's history—from 1 to 12 stores in 10 years, founded on strong principles 
of sustainability and fair trade. She reveals the core conflict: a debate within the management team (MT) about launching 
an online sales channel. She outlines three opposing options (full launch, no launch, small-scale pilot) and asks, 
"How do you take a good decision here?"
- **Scene 2**: Charina admits she loses sleep over the decision. She is torn between the impersonal nature of online sales 
and the potential exposure, and is worried about the impact on loyal staff. She then makes a direct request: 
"Can you perhaps chair our next MT meeting? So we can finally reach a decision together?"
- **Scene 3**: Charina acknowledges the candidate's input but states she is still not decided and finds it difficult. 
She presses for concrete next steps: "What do you mainly advise me? And what can you do for me? What should I tackle first, do you think?"
- **Scene 4**: Scene 4 is the final wrap-up instruction to the candidate, summarizing and closing the conversation.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Judgment Formation** - The candidate's ability to form a well-reasoned, balanced (mentioning both pros and cons), 
and fact-based judgment in response to Charina's complex situation.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The response is generic, illogical, or avoids forming a judgment. 
The candidate fails to distinguish between relevant and irrelevant information, 
provides no factual support for their statements, and does not acknowledge different sides of an issue.
- **2** (Fair): The candidate identifies basic, surface-level relevant aspects but struggles 
to prioritize them. Their reasoning is supported by vague references to facts rather than concrete details. 
They may state a standpoint but without a clear consideration of pros and cons.
- **3** (Satisfactory): The candidate distinguishes between relevant and irrelevant aspects 
of the situation (e.g., focuses on Charina's core dilemmas rather than tangential details). 
They support their reasoning by referring to specific facts from Charina's story or general logical principles. 
They begin to state a standpoint and acknowledge opposing arguments or pros and cons.
- **4** (Good): The candidate clearly prioritizes the most relevant aspects of the problem and filters out 
side issues. They actively use facts and details from Charina's story to build a logical argument for their advice. 
They explicitly state their standpoint and present a balanced view by discussing both the advantages 
and disadvantages of their proposed course of action.
- **5** (Excellent): The candidate demonstrates sophisticated judgment by seamlessly integrating 
the most critical, multi-faceted aspects of the problem. Their reasoning is compellingly supported 
by a synthesis of facts from all scenes, revealing underlying causes and implications. 
They clearly present a nuanced standpoint that thoroughly and fairly evaluates the pros and cons, 
leading to a well-justified, holistic recommendation.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Judgment Formation" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for personal priorities to form the basis of a judgment. 
Uses specific details to support their reasoning. Clearly advises a path forward while also discussing its potential downsides or challenges.

Transcript:
```{text}```
"""
    ),

    # --- Organisatiesensitiviteit (Organizational sensitivity) ---
    "AD_ORGANS": (
        "AD_ORGANS",
        """
        **Context of the role-playing exercise:**
You are a professional recruiter. Your task is to evaluate a job candidate based on their responses in an asynchronous 
video role-playing exercise. In this role-playing exercise, the candidate responds verbally to a fictional business owner 
named Charina, across three scenes. Charina shares a strategic dilemma about expanding her sustainable retail business online, 
describes conflicts within her management team, and asks the candidate for advice and direct support. More specifically:

- **Scene 1**: Charina explains the company's history—from 1 to 12 stores in 10 years, founded on strong principles 
of sustainability and fair trade. She reveals the core conflict: a debate within the management team (MT) about launching 
an online sales channel. She outlines three opposing options (full launch, no launch, small-scale pilot) and asks, 
"How do you take a good decision here?"
- **Scene 2**: Charina admits she loses sleep over the decision. She is torn between the impersonal nature of online sales 
and the potential exposure, and is worried about the impact on loyal staff. She then makes a direct request: 
"Can you perhaps chair our next MT meeting? So we can finally reach a decision together?"
- **Scene 3**: Charina acknowledges the candidate's input but states she is still not decided and finds it difficult. 
She presses for concrete next steps: "What do you mainly advise me? And what can you do for me? What should I tackle first, do you think?"
- **Scene 4**: Scene 4 is the final wrap-up instruction to the candidate, summarizing and closing the conversation.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
The text was automatically transcribed, so it may contain filler words, hesitation markers, 
partial sentences, and transcription glitches. 
Evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Organizational sensitivity** - The candidate's empathic concern, awareness of and consideration 
for the interpersonal dynamics, unspoken rules, and potential impact of their decisions 
on different people and parts of the organization within Charina's company.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 

- **1** (Poor): The candidate shows no awareness of organisational sensitivities. 
They ignore the team conflict, personal relationships, and the emotional impact of decisions. 
Their advice is given in a vacuum, without considering how it will be received or its consequences for others.
- **2** (Fair): The candidate acknowledges that sensitivities exist but does not explore them deeply. 
They offer superficial advice on considering others but lack a concrete plan to manage the impact. 
Their consideration of consequences is vague and not integrated into their proposed solutions.
- **3** (Satisfactory): The candidate actively identifies key sensitivities (e.g., the founder's 
relationship with her friend/co-founder, staff loyalty, the clash between personal values and business growth). 
They ask questions to understand these dynamics better and propose steps that show some forethought 
about reception and consequences.
- **4** (Good): The candidate demonstrates a clear and nuanced understanding of the organisational landscape. 
They proactively anticipate how different stakeholders (the co-founder, the marketing manager, long-term staff) 
will react to decisions. Their advice is carefully crafted to manage these sensitivities, build consensus, 
and mitigate negative consequences.
- **5** (Excellent): The candidate exhibits a sophisticated, systemic understanding of the organisation's 
interpersonal and cultural fabric. They treat the organisational sensitivities as a central part 
of the problem to be solved. Their approach is designed to heal rifts, rebuild trust, and ensure 
any decision is not only logical but also sustainable and widely supported because it respects 
the organisation's unique history and relationships.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors that reflect the "Organizational sensitivity" competency.
- Avoid defaulting to an average (3) unless no clear information is available.
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A short explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes the emotional and relational consequences of letting staff go 
  versus pivoting their roles, showing a deep consideration for the human impact.

Transcript:
```{text}```
"""
    )
}