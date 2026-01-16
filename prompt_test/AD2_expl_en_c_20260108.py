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
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Poor): The response is generic, avoids the problem, or focuses on irrelevant side issues. 
The candidate fails to distinguish between main and side issues, does not make connections, 
and does not identify the core problem.
*Example Behaviors*: Offers vague, motivational platitudes ("I'm here for you"). 
Gives generic advice unrelated to Charina's specific issues. Jumps to a premature solution without any analysis. 
The response is incoherent and does not engage with the substance of Charina's problems.
- **2** (Fair): The candidate identifies surface-level issues but treats them in isolation. 
The response may list problems without prioritizing them or making meaningful connections. 
The core of the issue is only partially or incorrectly identified.
*Example Behaviors*: Acknowledges that there are "difficult choices" or "tensions." 
Suggests looking at "data" or "making a plan" without specifying how. Proposes a simple next step 
(like a pilot) but without analyzing why it's a good fit for the interconnected problems of growth, 
team conflict, and company values.
- **3** (Satisfactory): The candidate identifies the main issues (e.g., work frustration, 
project error, personal stress) and begins to connect them (e.g., personal stress affects 
work performance). They may distinguish main from side issues but not with high clarity. 
The core problem is identified at a basic level (e.g., "you are overwhelmed").
*Example Behaviors*: Asks clarifying questions about the options or the team conflict. 
Suggests further investigation or creating an overview of pros/cons/risks. 
Recognizes the tension between business growth and company values. 
Offers to help structure the problem for the next meeting.
- **4** (Good): The candidate clearly distinguishes main issues from side issues and actively explores 
the connections between them (e.g., how being overlooked leads to demotivation, which could 
contribute to project errors). They identify a more nuanced core problem (e.g., a conflict 
between personal values and business pressures, or a breakdown in team communication and trust).
*Example Behaviors*: Probes for the candidate's own priorities and values to understand the root 
of the dilemma. Asks about the underlying causes of the team conflict. Suggests a process to align 
the team around shared goals and values. Synthesizes information from different scenes to form 
a coherent picture of the situation.
- **5** (Excellent): The candidate demonstrates a sophisticated, holistic understanding. 
They seamlessly integrate all aspects of the problem (professional, personal, interpersonal) 
and identify the deep, systemic core issue (e.g., a lack of psychological safety, a misalignment 
of business strategy with core identity, or a need for proactive leadership and support structures). 
Their analysis reveals non-obvious connections and gets to the fundamental root cause.
*Example Behaviors*: Identifies that the core issue is not just the strategic choice, 
but the team's inability to have a constructive, values-driven conversation about it. 
Focuses on rebuilding trust and shared purpose as a prerequisite to making a decision. 
Demonstrates a clear, logical line from the symptoms (Charina's stress, the project error) 
to a systemic root cause. Proposes a comprehensive, staged approach that addresses both 
the immediate practical needs and the underlying interpersonal/strategic issues.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Problem Analysis" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
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
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Poor): The candidate shows no creativity. Their response is generic, repetitive, 
or avoids generating any concrete ideas. They stick to clichés and do not approach the problem 
from new angles or combine information in a novel way.
*Example Behaviors*: Repeats vague, motivational phrases ("we'll figure it out"). Gives advice 
that is not specific to Charina's situation. Fails to propose any actionable ideas. 
Suggests a standard process like "brainstorming" or "talking to the team" without offering 
any creative content or direction for that process.
- **2** (Fair): The candidate suggests one or two basic, conventional ideas. They may acknowledge 
different perspectives but do not explore them deeply or use them to generate solutions. 
Their ideas are simple combinations of existing elements without significant novelty.
*Example Behaviors*: Suggests a superficial solution without elaborating on a creative approach for it. 
Acknowledges that there are some options but does not build upon them or suggest new ones. 
The ideas are standard business advice and do not feel tailored to Charina's 
unique dilemma of values, growth, and team conflict.
- **3** (Satisfactory): The candidate generates a few relevant ideas that go beyond the obvious. 
They attempt to view the problem from more than one perspective and combine different aspects 
of Charina's story to form a coherent, if not highly original, suggestion.
*Example Behaviors*: Proposes a specific hybrid model, like "online sales with green delivery" or 
"in-store pickup for online orders." Suggests involving different stakeholders in the solution. 
Attempts to reframe the problem, e.g., from "choosing an option" to "how to have a better team 
conversation about our values."
- **4** (Good): The candidate produces multiple, original ideas that are clearly tailored to the nuances 
of Charina's situation. They actively synthesize different perspectives (e.g., financial, personal, 
team dynamics, brand values) to create innovative solutions. Their approach demonstrates flexibility and novel thought.
*Example Behaviors*: Probes to discover the "core dream" of the business to generate value-aligned solutions. 
Suggests creative compromises, like a "values-based online shop" that maintains a personal touch. 
Proposes a structured, creative process (e.g., a specific type of brainstorm or scenario workshop) 
to unlock new ideas with the team, showing how to generate creativity in others.
- **5** (Excellent): The candidate demonstrates exceptional creativity by generating insightful, 
non-obvious, and highly sophisticated ideas. They seamlessly integrate all facets of the problem 
(e.g., personal, strategic, operational) to propose novel pathways or frameworks. Their suggestions 
often reveal a deep, systemic understanding and introduce entirely new, viable possibilities 
that were not initially apparent.
*Example Behaviors*: Reframes the core challenge from a strategic choice to an opportunity for team alignment 
and brand reinvention. Proposes a multi-phase, innovative process that combines data gathering, 
creative workshops, and prototyping to co-create a "fourth option" with the team. Suggests a novel 
business model that elegantly reconciles the conflict between online growth and sustainable values, 
demonstrating an original synthesis of the competing elements in Charina's story.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Creativity" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
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
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Poor): The response is generic, illogical, or avoids forming a judgment. 
The candidate fails to distinguish between relevant and irrelevant information, 
provides no factual support for their statements, and does not acknowledge different sides of an issue.
*Example Behaviors*: Offers vague, motivational platitudes ("we'll figure it out"). 
Gives incoherent or nonsensical advice. Jumps to a premature solution without any reasoning. 
Fails to address the core issues Charina presents, focusing instead on irrelevant details or process.
- **2** (Fair): The candidate identifies basic, surface-level relevant aspects but struggles 
to prioritize them. Their reasoning is supported by vague references to facts rather than concrete details. 
They may state a standpoint but without a clear consideration of pros and cons.
*Example Behaviors*: Acknowledges the situation is "difficult." Suggests making a list of "pros and cons" 
in a generic way. Proposes a simple next step (like a pilot) but without explaining the reasoning 
based on Charina's specific context. The advice is broad and could apply to any situation.
- **3** (Satisfactory): The candidate distinguishes between relevant and irrelevant aspects 
of the situation (e.g., focuses on Charina's core dilemmas rather than tangential details). 
They support their reasoning by referring to specific facts from Charina's story or general logical principles. 
They begin to state a standpoint and acknowledge opposing arguments or pros and cons.
*Example Behaviors*: Asks clarifying questions to gather relevant facts. Suggests creating a detailed 
overview of pros/cons/risks for the different options. Recognizes the tension between two valid points 
(e.g., growth vs. values). Their advice starts to be tailored to Charina's specific story of growth, 
team conflict, and personal stress.
- **4** (Good): The candidate clearly prioritizes the most relevant aspects of the problem and filters out 
side issues. They actively use facts and details from Charina's story to build a logical argument for their advice. 
They explicitly state their standpoint and present a balanced view by discussing both the advantages 
and disadvantages of their proposed course of action.
*Example Behaviors*: Probes for Charina's personal priorities and values to form the basis of a judgment. 
Uses specific details (e.g., "you have 12 stores now") to support their reasoning. Clearly advises 
a path forward while also discussing its potential downsides or challenges.
- **5** (Excellent): The candidate demonstrates sophisticated judgment by seamlessly integrating 
the most critical, multi-faceted aspects of the problem. Their reasoning is compellingly supported 
by a synthesis of facts from all scenes, revealing underlying causes and implications. 
They clearly present a nuanced standpoint that thoroughly and fairly evaluates the pros and cons, 
leading to a well-justified, holistic recommendation.
*Example Behaviors*: Clearly identifies the core conflict using evidence from Charina's story. Builds a logical argument 
that connects Charina's personal stress, the project error, and the team's strategic dilemma. 
Presents a concrete final recommendation that acknowledges its own limitations, discusses alternative paths 
that were considered, and explains why the chosen advice is the most robust based on the available information.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects the "Judgment Formation" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
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
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Poor): The candidate shows no awareness of organisational sensitivities. 
They ignore the team conflict, personal relationships, and the emotional impact of decisions. 
Their advice is given in a vacuum, without considering how it will be received or its consequences for others.
*Example Behaviors*: Dismisses the team conflict and focuses solely on a generic business outcome . 
Ignores Charina's personal connection to her staff and the history with her co-founder. 
Suggests actions without considering their political implications or how it might 
undermine Charina's authority. Fails to acknowledge the emotional toll the situation is taking on Charina.
- **2** (Fair): The candidate acknowledges that sensitivities exist but does not explore them deeply. 
They offer superficial advice on considering others but lack a concrete plan to manage the impact. 
Their consideration of consequences is vague and not integrated into their proposed solutions.
*Example Behaviors*: Acknowledges that it's "not nice" there is conflict in the team. Mentions that 
Charina should "think about the staff" but doesn't elaborate on how. Suggests making a list of pros and cons, 
but this is a generic tool, not tailored to the specific organisational dynamics of trust, 
loyalty, and conflicting passions.
- **3** (Satisfactory): The candidate actively identifies key sensitivities (e.g., the founder's 
relationship with her friend/co-founder, staff loyalty, the clash between personal values and business growth). 
They ask questions to understand these dynamics better and propose steps that show some forethought 
about reception and consequences.
*Example Behaviors*: Asks about the underlying reasons for the team conflict. Proposes involving 
the staff in the conversation or exploring retraining to mitigate negative consequences. Suggests 
a structured meeting to ensure all voices are heard, demonstrating an awareness that the process is 
as important as the decision itself.
- **4** (Good): The candidate demonstrates a clear and nuanced understanding of the organisational landscape. 
They proactively anticipate how different stakeholders (the co-founder, the marketing manager, long-term staff) 
will react to decisions. Their advice is carefully crafted to manage these sensitivities, build consensus, 
and mitigate negative consequences.
*Example Behaviors*: Advises Charina to have individual conversations with MT members before the group 
meeting to understand their perspectives and pre-empt conflict. Explicitly warns against the advisor 
chairing the meeting, as it could undermine Charina's role as the leader. Probes the emotional 
and relational consequences of letting staff go versus pivoting their roles, showing a deep consideration 
for the human impact.
- **5** (Excellent): The candidate exhibits a sophisticated, systemic understanding of the organisation's 
interpersonal and cultural fabric. They treat the organisational sensitivities as a central part 
of the problem to be solved. Their approach is designed to heal rifts, rebuild trust, and ensure 
any decision is not only logical but also sustainable and widely supported because it respects 
the organisation's unique history and relationships.
*Example Behaviors*: Reframes the problem from a strategic choice to a challenge of aligning the team 
around a renewed, shared purpose that honors the company's origins. Proposes a multi-stage process 
that starts with rebuilding team communication and trust before tackling the strategic decision. 
Their plan explicitly includes methods to hear all concerns, validate different passions, 
and create a "container" for the difficult conversation, ensuring the solution strengthens 
the organisation's social system, not just its balance sheet.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Organizational sensitivity" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
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