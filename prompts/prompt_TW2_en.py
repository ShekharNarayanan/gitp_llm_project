# Prompt for the competency of Teamwork 2 (actor: Marijne)
# The prompt is based on the strucure of the test prompt "AD2_expl_en_c_20260108.py"

promptTW_en = {
    # --- Samenwerken (Collaboration) ---
    "TW_SAMEN": (
        "TW_SAMEN",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate interacts with their colleague Marijne, who is friendly, energetic, 
and generally pleasant to work with. Two weeks ago, they started a joint assignment that requires close collaboration: 
together they must develop a new idea for the organization, produce a written report, and prepare a presentation. 
Time is running out, but they have not yet managed to properly align or plan the work. Across the scenes, 
Marijne repeatedly attempts to shift most of the workload to the candidate, questions the assignment’s value, 
and proposes a division of labor that emphasizes her preferred tasks while avoiding others. More specifically:

- **Scene 1**: Marijne opens warmly and quickly proposes that the candidate writes the report this week, 
including her section as well, because she is short on time due to other work and an upcoming client lunch. 
She frames the request as a compliment (the candidate being a “good writer”) and asks whether the candidate minds doing it. 
The candidate should respond to Marijne’s proposal to offload the report-writing and clarify how the work should be divided and planned.
- **Scene 2**: Marijne laughs off the urgency and suggests things will “work out,” while implying she might 
only have time next week, depending on another project that she says takes priority. She downplays the situation, 
avoids specifics, and questions whether colleagues even want the new idea and presentation. The candidate should 
respond to her casual attitude, the lack of commitment, and her doubts about the assignment’s relevance, 
and should ask questions to understand constraints and align on expectations.
- **Scene 3**: Marijne becomes explicit about her motivation: she says the assignment doesn’t challenge her enough 
and that she prefers investing her time in another project for her development. She states she wants to do the presentation 
because that’s where she feels strong, and proposes a collaboration model where the candidate does the research and report, 
while she presents the outcome. She frames this as “still working together” and challenges the candidate’s view by asking 
what collaboration means to them. The candidate should respond to this proposed imbalance and explain 
what they consider effective collaboration in this assignment.
- **Scene 4**: Marijne acknowledges the candidate’s point and suggests revisiting the task division. She says she needs to speak 
to the manager first to ensure she has enough time, noting a meeting in two days and proposing to update the candidate in three days. 
She then asks what else they agree on. The candidate should summarize the conversation, capture any agreements 
about responsibilities and timing, and wrap up with clear next steps and alignment points.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Collaboration** - The candidate’s ability for collaboration skills, such as offering to help Marijne, placing 
the collective interest above Marijne’s personal interest, or taking actions that promote collaboration.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little genuine collaboration. They do not actively build shared ownership, 
mutual support, or a “we” approach to the joint deliverable. Instead, they focus on pushing tasks, setting demands, 
or “dividing work” in a one-sided way, without aligning on goals, constraints, or how to work together. They fail to place 
the collective project interest above individual preferences, and they do not take concrete actions that improve collaboration. 
Interaction can feel controlling rather than cooperative.
*Example Behaviors*: Uses one-sided expressions (e.g., emphasizes “I expect you to make time” and “I want you to…”) 
rather than exploring Marijne’s capacity and jointly finding a workable plan. Treats collaboration as simply splitting tasks, 
with limited joint problem-solving or shared responsibility. Accepts an imbalanced or vague division (e.g., “you present, I analyze”) 
without ensuring equal contribution or mutual support. Uses accountability language (e.g., “if it doesn’t go well, tell me beforehand”) 
but offers minimal help (e.g., no concrete step to unblock time, no co-working session, no shared timeline). 
Focuses on compliance and coordination with a manager, not on strengthening teamwork.
- **2** (Poor): The candidate shows some collaborative intent, but collaboration is fragile and transactional. 
They focus mainly on fairness and correcting Marijne, rather than actively building shared ownership, trust, and momentum. 
Support is limited, and the candidate may escalate to pressure or threats instead of negotiating a workable plan. 
The collective interest is stated, but not translated into constructive joint working practices.
*Example Behaviors*: Pushes back on Marijne’s offloading and emphasizes equality (e.g., “we do it together,” “half-half”), 
yet frames it as an ultimatum (“e.g., together or not”) or implies blame (e.g., “you should’ve known at the start”). 
Talks about strengths, but mostly as a way to allocate tasks rather than co-developing the idea/report/presentation. 
Suggests going to the manager or sets hard deadlines (e.g., “by end of day”) without first creating a shared plan 
(e.g., co-working session, milestones, agreed timeline). Gives limited practical help to enable collaboration 
(e.g., no concrete alignment meeting, shared document structure, or coordinated next steps).
- **3** (Sufficient): The candidate demonstrates basic collaboration by keeping the joint nature of the assignment central 
and attempting to protect shared ownership. They respond to Marijne’s attempts to offload work by emphasizing that deliverables 
must be completed together, and they propose at least one workable way to align. They may show some willingness 
to help and acknowledge time pressure, but collaboration can still be somewhat reactive: the plan is only moderately detailed, 
the candidate sometimes slips into fairness talk, and joint working practices (milestones, shared drafts, coordination rhythm) are not consistently established.
*Example Behaviors*: Pushes back politely on “do my part too,” and suggests concrete coordination (e.g., “Let’s block an hour 
next week and decide tasks and timing”). Proposes a reasonable division with shared touchpoints (e.g., candidate drafts 
the report, Marijne provides input and reviews; presentation prepared together). Encourages checking manager availability 
and then returning with a time plan. References collective interest (e.g., quality of report/presentation, meeting deadline) 
and tries to keep both involved. May offer to take on a larger portion temporarily due to time pressure, but asks for 
at least minimal contributions (e.g., bullets, summary points, feedback) to maintain joint ownership.
- **4** (Good): The candidate demonstrates strong collaboration by actively protecting shared ownership of the assignment 
while keeping the relationship constructive. They acknowledge Marijne’s constraints, but consistently steer toward the collective goal 
(idea + report + presentation) and take concrete actions that promote working together. They offer support 
without enabling one-sided offloading. When Marijne resists or seeks credit-heavy tasks, the candidate handles it respectfully 
and negotiates a workable division that preserves quality and joint accountability.
*Example Behaviors*: Politely refuses to write Marijne’s section, but offers collaboration enablers (e.g., brief brainstorm call, 
shared outline, review/comments). Proposes concrete coordination (e.g., “let’s put calendars next to each other,” 
“block a half day,” “short online session”) and sets near-term milestones (e.g., draft by X date, joint review, presentation prep). 
Frames decisions around the team deliverable and fairness (e.g., “we both need to understand what we present”). 
Suggests involving the manager only to unblock capacity or clarify priority—without threatening. Summarizes clear next steps: 
who delivers what, when they meet, and how they’ll integrate and finalize together.
- **5** (Excellent): The candidate demonstrates high-impact collaboration that creates shared ownership, momentum, 
and mutual support, even when Marijne is busy or less motivated. They consistently place the collective deliverable 
(idea + report + presentation) above individual preferences, and they translate that into concrete collaborative actions 
(e.g., rapid alignment, realistic planning, balanced contribution, and frequent coordination points). They offer help 
in a way that enables Marijne (e.g., templates, draft outlines, short syncs) without taking over her work. They handle resistance 
constructively—reframing, negotiating trade-offs, and securing explicit commitments—while preserving a positive working relationship and clear accountability.
*Example Behaviors*: Proposes an immediate coordination step (e.g., “let’s open calendars now”) and sets a tight shared plan 
(e.g., deadlines for each part of the report; a 30-minute presentation outline session; a follow-up slot). Actively checks capacity 
(e.g., “you’re busy today/tomorrow—when can you deliver your section?”) and balances workload (e.g., “I’ll finish my part 
by Wednesday; you deliver yours Thu/Fri”). Shares resources to help Marijne succeed (e.g., sending a draft, outline, or example section), 
and sets joint checkpoints (e.g., review each other’s sections; split presentation chapters; rehearse together). 
Responds to “not challenging” by keeping collaboration intact (e.g., “we’ll finish this together, then pick a more challenging project”), 
without enabling one-sided credit-taking.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Collaboration" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Overtuigingskracht (Persuasiveness) ---
    "TW_OVERT": (
        "TW_OVERT",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes.  

In this role-playing exercise, the candidate interacts with their colleague Marijne, who is friendly, energetic, 
and generally pleasant to work with. Two weeks ago, they started a joint assignment that requires close collaboration: 
together they must develop a new idea for the organization, produce a written report, and prepare a presentation. 
Time is running out, but they have not yet managed to properly align or plan the work. Across the scenes, 
Marijne repeatedly attempts to shift most of the workload to the candidate, questions the assignment’s value, 
and proposes a division of labor that emphasizes her preferred tasks while avoiding others. More specifically:

- **Scene 1**: Marijne opens warmly and quickly proposes that the candidate writes the report this week, 
including her section as well, because she is short on time due to other work and an upcoming client lunch. 
She frames the request as a compliment (the candidate being a “good writer”) and asks whether the candidate minds doing it. 
The candidate should respond to Marijne’s proposal to offload the report-writing and clarify how the work should be divided and planned.
- **Scene 2**: Marijne laughs off the urgency and suggests things will “work out,” while implying she might 
only have time next week, depending on another project that she says takes priority. She downplays the situation, 
avoids specifics, and questions whether colleagues even want the new idea and presentation. The candidate should 
respond to her casual attitude, the lack of commitment, and her doubts about the assignment’s relevance, 
and should ask questions to understand constraints and align on expectations.
- **Scene 3**: Marijne becomes explicit about her motivation: she says the assignment doesn’t challenge her enough 
and that she prefers investing her time in another project for her development. She states she wants to do the presentation 
because that’s where she feels strong, and proposes a collaboration model where the candidate does the research and report, 
while she presents the outcome. She frames this as “still working together” and challenges the candidate’s view by asking 
what collaboration means to them. The candidate should respond to this proposed imbalance and explain 
what they consider effective collaboration in this assignment.
- **Scene 4**: Marijne acknowledges the candidate’s point and suggests revisiting the task division. She says she needs to speak 
to the manager first to ensure she has enough time, noting a meeting in two days and proposing to update the candidate in three days. 
She then asks what else they agree on. The candidate should summarize the conversation, capture any agreements 
about responsibilities and timing, and wrap up with clear next steps and alignment points.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Persuasiveness** - The candidate’s ability for persuasiveness skills, such as using arguments that align with Marijne’s interests, 
clearly articulating the benefits of their proposal for her, or discussing in an appropriate manner any resistance expressed by Marijne.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little to no persuasiveness. They fail to connect arguments to Marijne’s interests 
and do not clearly articulate benefits for her of contributing properly. Instead, they rely on demands, fairness statements, 
or vague coordination talk without making a compelling case. Resistance is not explored or reframed constructively; 
the tone can become rigid rather than persuasive. The result is low buy-in and weak movement toward collaboration.
*Example Behaviors*: Uses pressure and expectations (e.g., “I really expect you to make time,” “we both have to do just as much”) 
instead of showing why it helps Marijne (e.g., less last-minute stress, credible presentation, shared credit, learning). 
Repeats generic statements about “dividing tasks” without tailoring to her situation or offering trade-offs. Accepts or proposes 
imbalanced splits (e.g., she presents, candidate does research) without explaining why shared preparation benefits her. 
Handles resistance with commands (e.g., “just do our thing,” “come back tomorrow”) rather than negotiating options. 
Leaves Marijne unconvinced, with no motivating rationale beyond “it’s required” or “it’s fair.”
- **2** (Poor): The candidate makes some attempts to persuade Marijne, but the argumentation is weakly tailored to her interests. 
Benefits are mentioned only vaguely rather than clearly linking the proposal to what Marijne gains. Resistance 
is acknowledged but not convincingly reframed; the tone may drift into mild pressure, moralizing, or generic reassurance.
*Example Behaviors*: Uses generic lines (e.g., “we just have to do what’s expected”, “it doesn’t matter what others think”) 
rather than persuasive, interest-aligned reasons for Marijne to contribute. Proposes coordination (e.g., “meet end of week,” 
“talk in a few days”) but doesn’t make a compelling case for why acting now helps Marijne. Offers help in a limited or inconsistent way 
(e.g., “I can take a look,” “I’ll start prelim work”) without tying it to shared ownership or a clear payoff for her. Handles resistance 
with “do your part” framing rather than offering trade-offs (e.g., shorter sync, dividing into bite-size tasks, protecting her time while still ensuring meaningful contribution).
- **3** (Sufficient): The candidate is moderately persuasive: they respond to Marijne’s time pressure and resistance 
with reasonable arguments and propose a workable way forward. They articulate some benefits for Marijne, and they address 
objections in a generally appropriate manner. However, the persuasion is not consistently sharp or deeply tailored to Marijne’s personal drivers, 
and trade-offs are only partly negotiated. Buy‑in is achieved at a basic level, but not maximized.
*Example Behaviors*: Politely refuses to do everything alone and explains why Marijne’s input matters (e.g., “you shouldn’t 
present something you don’t stand behind”). Uses practical, mildly motivating benefits (e.g., “if we align now, the final version 
and presentation will go smoother”). Responds to “are colleagues waiting for this?” by suggesting a quick check of expectations 
before investing too much time, or reframing toward delivering value. Proposes concrete next steps (e.g., draft report, 
send for feedback, schedule a short sync, agree on a presentation split) and requests a simple commitment 
(e.g., provide availability / feedback after the manager meeting). May rely on general fairness/requirements and lacks 
a highly personalized pitch or stronger negotiation of commitment.
- **4** (Good): The candidate is convincingly persuasive by aligning arguments with Marijne’s interests (time pressure, 
reputation, efficiency, visibility, development) and by clearly explaining why the proposed approach benefits her. 
They acknowledge her resistance (busy schedule, low challenge, preference to present) and reframe it constructively without 
escalating conflict. The candidate offers realistic options and trade-offs while maintaining the core request: 
meaningful contribution beyond “just presenting.” The tone is firm-but-respectful and typically leads to clearer commitment.
*Example Behaviors*: Explains that Marijne presenting without contributing risks credibility and makes Q&A harder, 
while shared prep protects her reputation and reduces last-minute stress. Uses interest-aligned framing (e.g., “If we block 
a short slot now, we save time later and finish faster”). Responds to “not challenging” by reframing to learning value or efficiency 
(e.g., “Let’s close this neatly, then you can focus on your bigger project”). Proposes concrete, low-friction steps 
(e.g., 30-min online sparring, shared outline/draft, quick check-in after manager meeting) and asks for specific commitments 
(e.g., send input by X, confirm meeting time). Keeps the message motivating rather than threatening.
- **5** (Excellent): The candidate demonstrates high-impact, tailored persuasiveness that moves Marijne from hesitation 
to commitment while keeping the relationship constructive. They explicitly connect their proposal to Marijne’s interests 
(saving time, reducing stress, protecting reputation/credibility in the presentation, gaining fair recognition, freeing capacity 
for her preferred projects). They address resistance directly (busy schedule, “not challenging,” wanting only to present) 
and reframe it into a win–win plan with realistic choices and trade-offs. They make the benefits concrete and secure 
clear buy-in, keeping escalation (manager) as a last resort.
*Example Behaviors*: Clearly articulates why Marijne contributing beyond presenting benefits her (e.g., she can present confidently, 
handle questions, avoid last-minute panic, and share credit fairly). Uses time/efficiency framing (e.g., "If we align for 20–30 minutes now 
and split the work smartly, we’ll finish sooner and you can focus on your other project”). Offers options (e.g., short call today vs. 
focused block tomorrow; draft + quick edits; minimal-but-meaningful writing contribution) and negotiates commitments 
with deadlines. Responds by preventing delay (e.g., proposes meeting tomorrow and starting immediately, with manager 
involvement only if time/capacity truly can’t be created). Summarizes the deal crisply and checks agreement.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Persuasiveness" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Mondelinge communicatie (Oral communication) ---
    "TW_MONDEC": (
        "TW_MONDEC",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate interacts with their colleague Marijne, who is friendly, energetic, 
and generally pleasant to work with. Two weeks ago, they started a joint assignment that requires close collaboration: 
together they must develop a new idea for the organization, produce a written report, and prepare a presentation. 
Time is running out, but they have not yet managed to properly align or plan the work. Across the scenes, 
Marijne repeatedly attempts to shift most of the workload to the candidate, questions the assignment’s value, 
and proposes a division of labor that emphasizes her preferred tasks while avoiding others. More specifically:

- **Scene 1**: Marijne opens warmly and quickly proposes that the candidate writes the report this week, 
including her section as well, because she is short on time due to other work and an upcoming client lunch. 
She frames the request as a compliment (the candidate being a “good writer”) and asks whether the candidate minds doing it. 
The candidate should respond to Marijne’s proposal to offload the report-writing and clarify how the work should be divided and planned.
- **Scene 2**: Marijne laughs off the urgency and suggests things will “work out,” while implying she might 
only have time next week, depending on another project that she says takes priority. She downplays the situation, 
avoids specifics, and questions whether colleagues even want the new idea and presentation. The candidate should 
respond to her casual attitude, the lack of commitment, and her doubts about the assignment’s relevance, 
and should ask questions to understand constraints and align on expectations.
- **Scene 3**: Marijne becomes explicit about her motivation: she says the assignment doesn’t challenge her enough 
and that she prefers investing her time in another project for her development. She states she wants to do the presentation 
because that’s where she feels strong, and proposes a collaboration model where the candidate does the research and report, 
while she presents the outcome. She frames this as “still working together” and challenges the candidate’s view by asking 
what collaboration means to them. The candidate should respond to this proposed imbalance and explain 
what they consider effective collaboration in this assignment.
- **Scene 4**: Marijne acknowledges the candidate’s point and suggests revisiting the task division. She says she needs to speak 
to the manager first to ensure she has enough time, noting a meeting in two days and proposing to update the candidate in three days. 
She then asks what else they agree on. The candidate should summarize the conversation, capture any agreements 
about responsibilities and timing, and wrap up with clear next steps and alignment points.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Oral communication** - The candidate’s ability for oral communication skills, such as conveying the message 
in a way that Marijne can clearly understand, supporting their points with concrete examples, or logically distinguishing 
between primary and secondary issues when communicating with Marijne.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate’s oral communication is unclear and hard to follow. They ramble, repeat themselves, 
and use vague phrasing without specifying what actions are needed. They do not structure the message logically 
(main point → reasoning → concrete next step) and they fail to distinguish primary issues (deadlines, task division, alignment) 
from secondary or unrelated topics (team “messiness,” broad ambitions). Concrete examples are missing, and the listener (Marijne) 
would struggle to understand what is being asked of her and why. The conversation ends without a crisp summary or clear agreements.
*Example Behaviors*: Unclear explanations (e.g., “doing it together”, “helping with all my heart,”) without stating a clear proposal 
(e.g., who drafts what, when, and how they review). Shifts into unrelated, abstract themes (e.g., “putting the team on the map”) 
instead of focusing on the assignment deliverables. Uses ambiguous references with no concrete example of what might be misrepresented. 
Overloads the conversation with filler and repeated reassurance, but never provides a clear structure, prioritization, 
or actionable next step (e.g., a specific meeting time, a list of tasks, a short recap of agreements).
- **2** (Poor): The candidate’s message is partly understandable, but still lacks clear structure and precision. 
They communicate the general point (shared responsibility, need to meet/schedule, not taking over the whole report), 
yet the reasoning is often wordy, repetitive, or mildly confrontational. Primary issues (deadline, task division, next concrete step) 
are mixed with secondary points without clear prioritization. Examples are limited and often generic. The conversation 
may end with a meeting request, but without a crisp summary of agreements and deliverables.
*Example Behaviors*: Uses broad statements (e.g., “we have to do it,” “time is pressing,” “everyone does their part”), 
but doesn’t specify what that means (which section, how much, by when). Might shift between topics—planning, motivation, manager involvement, 
fairness—without signposting or sequencing. Communicates in a slightly accusatory way (e.g.,“pushing the work onto me,” 
“you should have started earlier”), which can reduce clarity and cooperation. Offers a meeting/poll for availability, yet gives no concrete agenda, 
milestones, or recap. Leaves Marijne with an incomplete picture of next steps and priorities.
- **3** (Sufficient): The candidate communicates in a generally clear and understandable way, with a basic logical structure 
(problem → proposal → next step). They can convey the main message to Marijne (shared responsibility, need to align, deadlines, task division) 
and usually keep the conversation on-topic. They sometimes support points with simple, concrete examples and can distinguish 
primary issues (planning, deliverables) from secondary ones (opinions of colleagues), though not always consistently. 
The message may still include some repetition or minor jumps, and summaries of agreements are present but can be somewhat broad.
*Example Behaviors*: States the core issue (e.g., “we’re not progressing / time is running out”), proposes a clear action 
(e.g., “block an hour next week / align after your manager meeting”), and explains why (e.g., “otherwise we miss the deadline / 
you shouldn’t present something you don’t stand behind”). Uses at least one concrete example to clarify 
(e.g., “if questions come after the presentation, you need to know the content”). Suggests a workable process 
(draft → feedback → final → presentation) and requests specific inputs (availability, feedback after manager talk). 
Ends with a basic recap of next steps (who drafts what, when they meet), but may not fully prioritize or tightly summarize all agreements.
- **4** (Good): The candidate communicates clearly, succinctly, and logically, making it easy for Marijne to understand 
what is expected and why. They structure the conversation around the primary issues (deadline, deliverables, fair task division, 
next coordination moment) and keep secondary topics clearly subordinated. They support key points with concrete examples 
and translate abstract “collaboration” into specific actions (drafts, review moments, time blocks). 
They summarize agreements crisply, including timelines and responsibilities, minimizing ambiguity.
*Example Behaviors*: States the core problem (e.g., “we’re behind and time is tight”), then proposes a clear plan 
(e.g., “15–30 min brainstorm after work; I draft an outline; you add your section by X; joint review end of week; presentation split next week”). 
Explains the rationale with a concrete example (e.g., “if questions come, you need to know the content, 
so you must contribute to the report”). Uses signposting (e.g., “first the report, then the presentation”) and separates 
must-haves from nice-to-haves (e.g., “manager discussion is useful, but we don’t wait to start”). 
Ends with a concise recap: what each person will do, by when, and when they reconnect.
- **5** (Excellent): The candidate’s oral communication is highly clear, concise, and structured, making the conversation 
easy for Marijne to follow and act on. They consistently distinguish primary issues (deadline, deliverables, fair contribution, 
concrete next steps) from secondary ones (colleagues’ enthusiasm, manager alignment) and use clear signposting (“first X, then Y”). 
They support key points with specific examples (e.g., why presenting without content ownership creates risks in Q&A, 
credibility, and rework). They translate abstract goals (“collaborate”) into actionable, time-bound steps, and close 
with a crisp recap of agreements (who/what/when), leaving no ambiguity.
*Example Behaviors*: States the purpose up front (e.g., “We need to finish report + presentation; time is tight”), 
then outlines a simple plan (e.g., “20‑min alignment today; draft outline by tomorrow; your section by Thursday; 
joint review Friday; slides split Monday”). Uses concrete examples to clarify reasoning (e.g., “If you present without writing input, 
you’ll struggle with questions and it can undermine credibility”). Keeps the discussion focused, redirecting tangents 
(e.g., “usefulness” is noted but parked until after the report outline). Summarizes at the end in bullet-like speech: 
deliverables, owners, deadlines, and the next meeting time, and checks understanding (e.g., “What did you capture as our agreements?”).

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Oral communication" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    ),

    # --- Organiseren eigen werk (Organization of own work) ---
    "TW_ORGANE": (
        "TW_ORGANE",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate interacts with their colleague Marijne, who is friendly, energetic, 
and generally pleasant to work with. Two weeks ago, they started a joint assignment that requires close collaboration: 
together they must develop a new idea for the organization, produce a written report, and prepare a presentation. 
Time is running out, but they have not yet managed to properly align or plan the work. Across the scenes, 
Marijne repeatedly attempts to shift most of the workload to the candidate, questions the assignment’s value, 
and proposes a division of labor that emphasizes her preferred tasks while avoiding others. More specifically:

- **Scene 1**: Marijne opens warmly and quickly proposes that the candidate writes the report this week, 
including her section as well, because she is short on time due to other work and an upcoming client lunch. 
She frames the request as a compliment (the candidate being a “good writer”) and asks whether the candidate minds doing it. 
The candidate should respond to Marijne’s proposal to offload the report-writing and clarify how the work should be divided and planned.
- **Scene 2**: Marijne laughs off the urgency and suggests things will “work out,” while implying she might 
only have time next week, depending on another project that she says takes priority. She downplays the situation, 
avoids specifics, and questions whether colleagues even want the new idea and presentation. The candidate should 
respond to her casual attitude, the lack of commitment, and her doubts about the assignment’s relevance, 
and should ask questions to understand constraints and align on expectations.
- **Scene 3**: Marijne becomes explicit about her motivation: she says the assignment doesn’t challenge her enough 
and that she prefers investing her time in another project for her development. She states she wants to do the presentation 
because that’s where she feels strong, and proposes a collaboration model where the candidate does the research and report, 
while she presents the outcome. She frames this as “still working together” and challenges the candidate’s view by asking 
what collaboration means to them. The candidate should respond to this proposed imbalance and explain 
what they consider effective collaboration in this assignment.
- **Scene 4**: Marijne acknowledges the candidate’s point and suggests revisiting the task division. She says she needs to speak 
to the manager first to ensure she has enough time, noting a meeting in two days and proposing to update the candidate in three days. 
She then asks what else they agree on. The candidate should summarize the conversation, capture any agreements 
about responsibilities and timing, and wrap up with clear next steps and alignment points.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Organizing own work** - The candidate’s ability to organize their own work, such as setting clear priorities 
in their own work by addressing important tasks first, adhering to the initial agreements made with Marijne in carrying out 
their own work, or informing Marijne in a timely manner when their workload prevents them from taking on new tasks.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate demonstrates poor self-organization and does not manage their own workload 
in a way that supports the joint project. They do not set clear priorities, do not translate “busy schedule” into a concrete plan, 
and do not adhere to (or help establish) initial agreements with Marijne. Communication about capacity is vague 
and not timely or actionable (no realistic time blocks, no deadlines, no deliverables). The candidate may overpromise 
without clarifying when or how, creating risk for delays and confusion. Overall, there is no reliable personal planning, 
no ownership of tasks, and no effective workload signaling.
*Example Behaviors*: Talks in generalities (e.g., says they are “really busy”, talk about “good planning”) 
but does not propose specific priorities (e.g., outline first, report draft next, slides last) or commit to concrete time slots. 
Defers coordination (e.g., “in a few days we’ll set an appointment”) without taking immediate organizing steps 
(e.g., calendar invite, milestone schedule, task list). Offers unclear task commitments (e.g., “I can pick up things,” 
“prepare a big part”) without defining what part, by when, or how it fits with other obligations. Fails to flag constraints 
early enough to protect the deadline, and does not provide a crisp update on what they can/cannot deliver—leaving Marijne 
with uncertainty and forcing her to carry the coordination burden.
- **2** (Poor): The candidate shows some awareness of workload and planning, but their self-organization is inconsistent 
and weakly operationalized. They communicate that they are busy and express willingness to help, yet they do not set clear priorities 
for their own work on the project, nor do they convert availability constraints into a concrete, reliable plan 
(time blocks, milestones, deliverables). They may overcommit without a realistic schedule, or defer action 
while the deadline approaches. Updates to Marijne are not timely enough to prevent delays, and agreements remain too vague to hold.
*Example Behaviors*: Uses non-specific language (e.g., says “I’m busy too” and proposes to “find a moment”) 
but doesn’t immediately send a calendar invite or reserve a specific slot. Offers to write (parts of) Marijne’s chapter 
or “carry” the work, creating scope creep instead of protecting priorities. Waits for Marijne’s manager conversation 
before progressing, rather than making an interim plan (outline now, drafts by X). Communicates intentions 
without concrete deliverables or timelines. Pushes for quicker answers from Marijne but doesn’t show their own 
structured plan (what they will finish today/tomorrow), leaving coordination and risk management mostly to the other person.
- **3** (Sufficient): The candidate shows basic self-organization: they acknowledge workload constraints, set some priorities, 
and take ownership of at least part of the work. They generally keep to initial agreements or renegotiate them when needed 
and communicate with Marijne about coordination points. However, planning is only moderately structured: 
milestones and time blocks may be present but not tightly defined, and the candidate may occasionally offer to cover 
too much or rely on broad timing rather than concrete deliverables and dates.
*Example Behaviors*: States they will start on the report/research and gives a basic reasoned priority (e.g., “we need 
to get started now; deadline is coming”). Proposes a workable coordination rhythm (e.g., “I draft first, then we review together,” 
“let me know after your manager talk and we align”). Communicates capacity constraints (e.g., “I can’t take your entire chapter; 
I can sketch broad strokes and you review/edit”) and asks for timely feedback. Suggests at least one planning step 
(e.g., schedule a meeting, share drafts, confirm who does which chapter), but may not always lock in exact deadlines, 
calendar invites, or clear success checkpoints for each deliverable.
- **4** (Good): The candidate demonstrates solid self-organization by translating the joint assignment into a clear 
personal plan with priorities, milestones, and timely updates to Marijne. They protect their capacity (do not overpromise), 
adhere to earlier agreements (or renegotiate them explicitly when constraints arise), and proactively schedule coordination moments. 
They focus first on high‑impact tasks and make sure Marijne is informed early if workload threatens commitments. 
Overall, the candidate’s actions reduce uncertainty and keep the project on track through concrete planning and dependable follow-through.
*Example Behaviors*: Sets priorities explicitly (e.g., “first align on report scope and chapter split, then draft chapters, 
then presentation”). Books a specific coordination slot this week (e.g., Thursday afternoon) and asks Marijne to confirm, 
rather than leaving it open-ended. States clear boundaries (e.g., “I can’t write the full report”) while committing to concrete deliverables 
(e.g., draft outline by X, own chapter by Y). Requests timely updates after Marijne’s manager meeting and uses that information 
to adjust the plan immediately. Maintains balanced ownership by insisting on agreed contributions and following 
through on their own tasks, reducing last-minute surprises.
- **5** (Excellent): The candidate demonstrates exceptional self-organization under time pressure. They translate 
the assignment into a clear personal plan with priorities, time blocks, deliverables, and checkpoints, and they reliably follow through. 
They explicitly protect capacity (no overpromising), adhere to the initial agreements (or renegotiate them immediately and transparently), 
and keep Marijne informed early when workload threatens progress. They proactively prevent drift by setting a short feedback cadence, 
and by converting “busy” into concrete commitments (“I will deliver X by Y”). Their approach reduces coordination load for Marijne and keeps the project on track.
*Example Behaviors*: States boundaries and commitments clearly (e.g., “I can’t take your chapter; I’ll complete my chapter by [day] 
and we review together [day/time]”). Pushes for timely updates (e.g., “don’t wait several days—update me right after your manager talk”) 
and schedules a near-term check-in (e.g., “end of this week we meet to see where we are”). Maintains ownership 
and prevents scope creep (e.g., “stick to what we agreed; if you’re stuck, signal early”). Sets priorities explicitly 
(report/chapters first, then slides) and uses a simple control loop (draft → feedback → final). Communicates capacity 
constraints early and proposes an adjustment plan (e.g., redistribute work, tighten deadlines) before the deadline is at risk.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Organizing own work" competency.
- Map the candidate's performance to the rubric above, using the behavioral examples as a guide.
- Avoid defaulting to an average (3) unless no clear information is available.
- Distribute scores across the scale based on actual performance differences. 
- Use the full 1-5 scale appropriately.
- Return **both**:
  1. The numeric rating (1-5, may include one decimal, e.g., 3.8).
  2. A detailed explanation (max 80 words) justifying the rating.
- Format your answer like this example:
  Rating: 4.2 - Explanation: The participant probes for the candidate's own priorities and values to understand the root of the dilemma.
  Synthesizes information from different scenes to form a coherent picture of the situation.

**Check for consistency**:
- Double-check that each score aligns with both the rubric criteria and the rationale provided.
- Maintain objectivity by strictly adhering to the rubric as written, without introducing personal interpretations or biases.

Transcript:
```{text}```
"""
    )
}