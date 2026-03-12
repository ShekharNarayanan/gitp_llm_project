# Prompt for the competency of Team Management 2 (actor: Daan)
# The prompt is based on the strucure of the test prompt "AD2_expl_en_c_20260108.py"

promptTM_en = {
    # --- Overtuigingskracht (Persuasiveness) ---
    "TM_OVERT": (
        "TM_OVERT",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Daan. Daan has been in the team 
for a few years and is generally known as positive and hardworking, but lately he has been less visible. 
He missed the weekly team meeting that morning without informing anyone. The team meeting is considered 
important because it is where plans for the coming week are discussed. The candidate has asked Daan 
to stop by to address what happened. More specifically:

- **Scene 1**: The conversation starts with Daan trying to avoid the topic and end it quickly because he is busy. 
He explains his absence as a deliberate choice, arguing the meeting often feels inefficient (unclear agenda, 
too much small talk) and saying he had other priorities (e.g., an important call). He also implicitly challenges 
the value of the meeting. The candidate should respond to Daan’s decision to skip the meeting without 
notice and his framing of the meeting as not worth his time.
- **Scene 2**: Daan partially acknowledges he should have been there, but immediately shifts to overload 
and reduced capacity. He describes having no peace at home or work, poor sleep, difficulty getting things done, 
and low energy. He reacts to the issue being raised as “making a fuss,” and asks to postpone: “Can’t we have 
this conversation another time?” The candidate should respond to Daan’s request to delay while also 
addressing the seriousness of the missed meeting and the signals of stress and disengagement.
- **Scene 3**:  Daan shares more detail about what is going on. He says his ex-partner is challenging 
the visitation arrangement for the kids, which is causing a lot of stress. He also mentions organizational changes 
and expresses frustration (e.g., “pffffffffff”), including a new system the team has to use that he finds difficult. 
He admits he missed the user training and says he doesn’t know how to handle everything right now. He asks directly: 
“Can you do something to help me?” The candidate should respond to Daan’s situation, including both the personal 
stressors and the work-related challenges (missed training, new system).
- **Scene 4**: Daan indicates he understands and thanks the candidate, but says he needs to get back to work soon. 
He asks for clarity and a recap: “So what exactly did we agree on, and what do you expect from me now?” 
The candidate should summarize the conversation, confirm any agreements made, and wrap up with clear expectations and next steps.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Persuasiveness** - The candidate’s ability for persuasiveness skills, such as using arguments that align with Daan’s interests, 
clearly articulating the benefits of their proposal for him, or discussing in an appropriate manner any resistance expressed by Daan.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little to no persuasiveness. They do not use arguments that connect to Daan’s interests, 
and they fail to clearly explain why a proposed approach benefits him or the team. Resistance is not addressed in a constructive way; 
instead the candidate stays vague, asks generic questions, and leans on guilt/need-based framing without making a compelling case. 
The conversation lacks concrete reasoning, options, or an “if–then” approach that could reduce Daan’s defensiveness and increase buy-in.
*Example Behaviors*: Uses broad, non-specific language (e.g., “talk about it sometime”) rather than persuasive, tailored reasons. 
Repeats concern and curiosity (e.g., “I’m worried,” “tell me more”) but does not offer a clear proposal with benefits for Daan 
(e.g., how meeting attendance helps him plan work, how support will reduce pressure). Relies on pressure statements 
(e.g., “I really need you to reach team performance”) instead of addressing Daan’s likely objections. Does not reframe 
resistance or negotiate realistic steps; no concrete incentives, trade-offs, or clear rationale is provided to motivate commitment.
- **2** (Poor): The candidate shows some attempts to persuade Daan, but the argumentation is weakly tailored to Daan’s interests 
and does not clearly articulate the benefits of compliance for him. Resistance is acknowledged but not worked through (e.g., the candidate 
may empathize and propose generic solutions, yet they do not reframe Daan’s objections or negotiate a realistic commitment). 
Overall, the approach is supportive but not convincingly persuasive.
*Example Behaviors*: Use broad statements (e.g., “team meetings are important”) and asks for ideas to make them more efficient, 
but doesn’t link attendance to Daan’s personal payoff (e.g., fewer ad‑hoc interruptions, clearer priorities). Focuses heavily on wellbeing 
(e.g., “take it easy,” “I’m worried”) and offers general help (e.g., confidential counselor, coffee chat, workload relief, training) 
without tying it to a clear ask (e.g., notifying absence, attending next meeting). Responds to resistance with vague follow-up 
(e.g., “schedule another moment,” “keep in touch”) rather than addressing the “waste of time” objection with concrete changes or trade-offs. 
Persuasion relies on concern, not a compelling, interest-aligned case.
- **3** (Sufficient): The candidate is moderately persuasive: they address Daan’s resistance and provide reasonable arguments 
for desired behavior, with some alignment to Daan’s interests. They acknowledge Daan’s stress and home situation and use this 
to motivate a practical path forward. Benefits are explained at a basic level. However, persuasion is not yet consistently sharp: 
objections are only partly reframed, and the “deal” is not fully negotiated.
*Example Behaviors*: Explains that the team meeting helps align weekly priorities, prevents missed information, and saves time later 
(e.g., “otherwise others must fill you in”). Validates Daan’s pressure and proposes supportive options (e.g., redo training, 
colleague help, task reprioritization, brief check-ins) while still making a clear ask (e.g., attend next meeting or notify absence in advance). 
Asks what would make meetings more effective and invites Daan’s input, but doesn’t fully translate that into a concrete meeting redesign. 
Summarizes with clear next steps (e.g., training arranged, follow-up appointment) and a basic commitment request, 
without a strong, tailored benefit pitch or firm negotiation of trade-offs.
- **4** (Good): The candidate is convincingly persuasive by aligning arguments with Daan’s interests and the realities he faces, 
while still addressing team norms (attendance, notifying absence). They acknowledge resistance and reframe it into a workable, 
beneficial proposal. Benefits for Daan are clearly articulated. The candidate discusses resistance 
appropriately—firm but supportive—and negotiates realistic commitments and trade-offs.
*Example Behaviors*: Explains that attending the weekly meeting helps Daan save time later (e.g., clear priorities, fewer ad-hoc updates, 
less duplication) and protects his workload planning. Directly addresses the “unclear agenda” objection by proposing concrete 
improvements (e.g., shorter meeting, fixed agenda, action list; Daan can contribute items). Sets a clear ask with rationale 
(e.g., notify in advance if absent and be present next time because his input strengthens decisions). Links support offers 
(e.g., buddy for the new system, catch-up training, temporary workload adjustment, short check-ins) to Daan’s payoff 
(e.g., reduced stress and quicker return to normal performance). Summarizes a practical deal: what Daan does, what the manager does, and by when.
- **5** (Excellent): The candidate demonstrates high-impact, tailored persuasiveness that shifts Daan from resistance 
to commitment without escalation. They quickly diagnose Daan’s underlying drivers and build a persuasive case that explicitly 
aligns with those interests. They reframe the team meeting from “waste of time” into a concrete tool for saving Daan time, 
reducing ad‑hoc disruptions, and protecting his focus. They handle resistance with calm firmness, offer credible choices/trade-offs, 
and negotiate a clear “deal” (standards + support) that Daan can realistically accept. The close includes explicit buy‑in, contingencies, and a confidence‑building tone.
*Example Behaviors*: Acknowledges Daan’s efficiency logic (e.g., “you don’t want time sinks”) and reframes (e.g., “Skipping creates 
more follow-up, ambiguity, and interruptions—attending prevents that”). Presents options (e..g, shorter meeting, fixed agenda, 
time-boxed round, pre-read, action list) while keeping the non‑negotiable norm (e.g., notify absence; attend unless agreed otherwise). 
Links benefits to Daan (e.g., fewer surprises, clearer priorities, less rework, more control over workload). Uses resistance respectfully 
(e.g., “what would make it worth it?”) and turns it into co-owned improvements. Negotiates concrete commitments 
(e.g., next meeting attendance + advance notice + system catch-up plan) and closes with a tight summary, deadlines, and a check-in plan (“if X happens, we do Y”).

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

    # --- Leidinggeven (Leadership) ---
    "TM_LEIDIN": (
        "TM_LEIDIN",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes.  

In this role-playing exercise, the candidate speaks with their employee Daan. Daan has been in the team 
for a few years and is generally known as positive and hardworking, but lately he has been less visible. 
He missed the weekly team meeting that morning without informing anyone. The team meeting is considered 
important because it is where plans for the coming week are discussed. The candidate has asked Daan 
to stop by to address what happened. More specifically:

- **Scene 1**: The conversation starts with Daan trying to avoid the topic and end it quickly because he is busy. 
He explains his absence as a deliberate choice, arguing the meeting often feels inefficient (unclear agenda, 
too much small talk) and saying he had other priorities (e.g., an important call). He also implicitly challenges 
the value of the meeting. The candidate should respond to Daan’s decision to skip the meeting without 
notice and his framing of the meeting as not worth his time.
- **Scene 2**: Daan partially acknowledges he should have been there, but immediately shifts to overload 
and reduced capacity. He describes having no peace at home or work, poor sleep, difficulty getting things done, 
and low energy. He reacts to the issue being raised as “making a fuss,” and asks to postpone: “Can’t we have 
this conversation another time?” The candidate should respond to Daan’s request to delay while also 
addressing the seriousness of the missed meeting and the signals of stress and disengagement.
- **Scene 3**:  Daan shares more detail about what is going on. He says his ex-partner is challenging 
the visitation arrangement for the kids, which is causing a lot of stress. He also mentions organizational changes 
and expresses frustration (e.g., “pffffffffff”), including a new system the team has to use that he finds difficult. 
He admits he missed the user training and says he doesn’t know how to handle everything right now. He asks directly: 
“Can you do something to help me?” The candidate should respond to Daan’s situation, including both the personal 
stressors and the work-related challenges (missed training, new system).
- **Scene 4**: Daan indicates he understands and thanks the candidate, but says he needs to get back to work soon. 
He asks for clarity and a recap: “So what exactly did we agree on, and what do you expect from me now?” 
The candidate should summarize the conversation, confirm any agreements made, and wrap up with clear expectations and next steps.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Leadership** - The candidate’s ability for leadership skills, such as creating clarity about the expected performance of Daan,
recognizing and expressing appreciation for any good performance of Daan, or adapting their own leadership style to Daan’s specific situation.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little effective leadership in this situation. They fail to create clear expectations 
about required performance, and they do not set or reinforce team norms. They either avoid the issue, become overly harsh, 
or focus only on Daan’s personal situation without connecting it back to work expectations. Appreciation for Daan’s historical 
strengths is absent or generic, and the leadership style is poorly adapted—either dismissing Daan’s stress/resistance 
or over-accommodating without accountability. The conversation ends without concrete agreements, timelines, or follow-up.
*Example Behaviors*: Does not address that Daan skipped the meeting without notice, or mentions it vaguely (e.g., “try to be there”) 
without stating what must change. Lets Daan shut down the conversation (e.g., “not a good time”) without re-establishing 
boundaries or scheduling a firm follow-up. Uses guilt (e.g., “we need you”) or moralizing rather than clear standards and support. 
Ignores Daan’s resistance (e.g., “meetings are a waste”) or responds defensively, escalating tension. Offers no specific next steps 
(e.g., notify in advance, attend next meeting, check-in plan, training catch-up) and does not summarize expectations or agreements before closing.
- **2** (Poor): The candidate shows some leadership intent, but creates only partial clarity about expected performance 
and team norms. Expectations are often phrased broadly without specifying standards, consequences, or a concrete monitoring plan. 
Appreciation is present yet often generic and not linked to specific behaviors to repeat. Adaptation to Daan’s situation is uneven: 
the candidate empathizes and offers support, but may over-accommodate and reduce accountability. Agreements tend to be vague or incomplete.
*Example Behaviors*: Focuses heavily on Daan’s wellbeing and offers help (e.g., time off, redistributing tasks, referral to support services) 
while giving only a loose instruction about meetings (e.g., “try to be there,” “cancel if you can’t”). Mentions meeting importance 
or social value, but doesn’t set clear expectations like notify beforehand, attend unless pre-agreed, or how missed info will be handled. 
Gives praise (e.g., “valued colleague,” “good ideas”) without connecting it to concrete performance requirements. 
Closes with broad next steps (e.g., schedule another talk, arrange training) but limited specificity on timing, responsibilities, 
and follow-up checks to ensure Daan’s reliability improves.
- **3** (Sufficient): The candidate demonstrates basic leadership by addressing the missed team meeting and creating 
reasonable clarity about expectations. They show some appreciation for Daan’s usual contribution, and they adapt 
their approach by acknowledging Daan’s stress/private situation and offering practical support. Expectations and agreements are present 
but may remain somewhat general. Overall, the candidate balances empathy and accountability at an acceptable level and ends with at least one concrete next step.
*Example Behaviors*: States that the weekly meeting is important for alignment and asks Daan to attend next time or inform 
the team in advance if he cannot. Recognizes Daan’s prior strengths (e.g., “normally positive/hardworking,” “your input is valuable”) 
and thanks him for openness. Responds to Daan’s situation by proposing support options (e.g., redo user training, buddy/colleague help, 
task overview and reprioritization, short check-ins). Summarizes agreements with a timeframe (e.g., follow-up next week; 
provide availability for training; make a task list), but may not fully specify what “acceptable attendance/communication” looks like 
in edge cases or how progress will be monitored beyond a general check-in.
- **4** (Good): The candidate demonstrates strong leadership by combining clear performance expectations with a supportive, 
situation-adapted approach. They explicitly set and explain team norms, and they clarify what Daan must do differently going forward. 
They also show specific appreciation for Daan’s value and link it to expectations. They adapt their style to Daan’s stress and private 
situation without letting accountability slip: empathy, boundaries, and practical support are balanced. Follow-up is structured with concrete steps and timeframes.
*Example Behaviors*: Addresses the missed meeting directly and sets a clear standard (e.g., meetings are important; 
if Daan can’t attend, he must notify in advance and possibly provide availability/alternative update). Acknowledges Daan’s current strain 
and invites disclosure at a level he’s comfortable with, while keeping the focus on workable solutions. Offers concrete support 
tailored to the situation (e.g., redo training, assign a buddy, reduce workload temporarily, check-in schedule, coordinate with HR/support services). 
Uses meaningful recognition (e.g., “your expertise matters,” “you used to be very steady/positive”) to motivate re-engagement. 
Ends with explicit agreements: what Daan will do (e.g., attendance/notice, training/buddy, signal overload early), what the manager will do, and when they will review progress.
- **5** (Excellent): The candidate shows outstanding leadership by combining high clarity, high empathy, and high accountability. 
They set crystal-clear performance standards and explain the rationale while calibrating tone to Daan’s stress and resistance. 
They give specific, credible appreciation and use it to reinforce expectations. They adapt their style dynamically: de-escalate, 
listen, diagnose root causes, and move quickly to a concrete, sustainable plan with ownership on both sides. 
Follow-up includes checkpoints and contingency actions.
*Example Behaviors*: Names the norm and boundary clearly (e.g., “Missing without notice isn’t OK; if you can’t attend, 
you message me/the team beforehand and we agree an alternative update”). Acknowledges Daan’s load and invites disclosure 
with choice (e.g., “share what you’re comfortable with; we can still solve work impact”). Connects appreciation to expectations 
(e.g., “your input raises the team’s quality; we rely on your predictability”). Co-creates a plan (e.g., immediate meeting 
update method, training catch-up + buddy, temporary reprioritization, and a short weekly check-in). Defines success indicators 
(e.g., attendance/notice rate, training completion, reduced last-minute issues) and states what happens if it slips 
(e.g., extra support, workload adjustment, escalation to HR). Summarizes agreements sharply with dates.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Leadership" competency.
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

    # --- Coachen (Coaching) ---
    "TM_COACH": (
        "TM_COACH",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Daan. Daan has been in the team 
for a few years and is generally known as positive and hardworking, but lately he has been less visible. 
He missed the weekly team meeting that morning without informing anyone. The team meeting is considered 
important because it is where plans for the coming week are discussed. The candidate has asked Daan 
to stop by to address what happened. More specifically:

- **Scene 1**: The conversation starts with Daan trying to avoid the topic and end it quickly because he is busy. 
He explains his absence as a deliberate choice, arguing the meeting often feels inefficient (unclear agenda, 
too much small talk) and saying he had other priorities (e.g., an important call). He also implicitly challenges 
the value of the meeting. The candidate should respond to Daan’s decision to skip the meeting without 
notice and his framing of the meeting as not worth his time.
- **Scene 2**: Daan partially acknowledges he should have been there, but immediately shifts to overload 
and reduced capacity. He describes having no peace at home or work, poor sleep, difficulty getting things done, 
and low energy. He reacts to the issue being raised as “making a fuss,” and asks to postpone: “Can’t we have 
this conversation another time?” The candidate should respond to Daan’s request to delay while also 
addressing the seriousness of the missed meeting and the signals of stress and disengagement.
- **Scene 3**:  Daan shares more detail about what is going on. He says his ex-partner is challenging 
the visitation arrangement for the kids, which is causing a lot of stress. He also mentions organizational changes 
and expresses frustration (e.g., “pffffffffff”), including a new system the team has to use that he finds difficult. 
He admits he missed the user training and says he doesn’t know how to handle everything right now. He asks directly: 
“Can you do something to help me?” The candidate should respond to Daan’s situation, including both the personal 
stressors and the work-related challenges (missed training, new system).
- **Scene 4**: Daan indicates he understands and thanks the candidate, but says he needs to get back to work soon. 
He asks for clarity and a recap: “So what exactly did we agree on, and what do you expect from me now?” 
The candidate should summarize the conversation, confirm any agreements made, and wrap up with clear expectations and next steps.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Coaching** - The candidate’s ability for coaching skills, such as helping Daan to gain insight into his strengths and weaknesses, 
encouraging him to develop himself and take on new challenges, or providing the space he needs to work on his development in his own way.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate demonstrates little to no real coaching. They do not help Daan gain insight 
into why his behavior has changed, what his strengths are, or what development would help him function better. 
Questions remain shallow and do not lead to reflection, ownership, or learning. The response does not explore Daan’s perspective, 
barriers, or preferred way of improving. Development is treated as compliance rather than a supported learning process. 
There is minimal space for Daan to shape next steps in his own way.
*Example Behaviors*: Focuses on correcting behavior (e.g., “not okay you didn’t call in”) and gives directive instructions 
(e.g., “redo training,” “apply it immediately,” “get help with your ex”) with little exploration of Daan’s self-assessment or patterns. 
Asks generic questions about whether he talks to someone, but doesn’t follow up to build insight or identify specific 
weaknesses/skills to develop. Offers solutions that are not personalized (e.g., assign “someone you trust,” 
“go to the doctor”) and frames private stress mainly as something to “put aside” for work. Ends with a list of expectations 
rather than a coaching plan (e.g., goals, small practice steps, reflection, and a supportive check-in).
- **2** (Poor): The candidate shows some coaching intent, but coaching remains surface-level and quickly shifts to instructions 
or practical fixes. They do not help Daan meaningfully reflect on patterns, nor do they translate insights into self-chosen 
development goals. Strengths are mentioned only generally, without using them to build a learning plan. 
The candidate provides some space, but ownership stays vague and practice steps are not clearly shaped around Daan’s way of working.
*Example Behaviors*: Emphasizes rules (e.g., “be present,” “let me know beforehand”) and proposes generic solutions 
(e.g., redo training, redistribute tasks, schedule a separate talk, refer to external support) without guiding Daan to identify 
his triggers and coping strategies. Asks broad questions (e.g., “what do you need?” “what’s going on?”) 
but doesn’t probe further to help Daan name concrete weaknesses to work on (e.g., planning, communication, 
escalation when overloaded). Provides encouragement (e.g., “take care of yourself”, offers time off), 
yet doesn’t co-create a development path (e.g., small experiments, reflection, feedback loop). 
Ends with vague agreements and limited follow-up on learning progress.
- **3** (Sufficient): The candidate demonstrates basic coaching by helping Daan reflect on what is happening and what 
he needs to move forward. They ask relevant questions about drivers behind his behavior and create some space 
for Daan to share, while keeping the conversation constructive. They identify development needs at a general but usable level 
and encourage Daan to take ownership. The coaching is supportive, but the development pathway is not yet highly structured.
*Example Behaviors*: Invites reflection (e.g., “this isn’t like you—what changed?”; “what is keeping you awake?”; 
“what do you need to move forward?”) and acknowledges strengths (e.g., “normally reliable/positive,” “your input matters”). 
Encourages Daan to take steps such as mapping tasks and overload signals, identifying what can be delegated, 
and planning how to communicate earlier when he can’t attend. Offers at least one concrete support action 
(e.g., catch-up user training, buddy/colleague support, short follow-up meeting) and requests a simple commitment 
(e.g., provide availability, inform manager, attend next meeting if possible). Summarizes next steps and schedules a follow-up, 
but may not yet specify small practice exercises, success indicators, or structured self-reflection.
- **4** (Good): The candidate provides structured, individualized coaching that helps Daan build insight into what is driving 
his recent behavior and how this affects his reliability and collaboration. They explicitly surface Daan’s strengths 
and connect them to development goals. The candidate gives Daan space to choose what to share and supports autonomy 
by co-creating next steps that fit him, with a clear follow-up and learning focus.
*Example Behaviors*: Uses reflective questions that deepen insight (e.g., “What has changed compared to when it went well?” 
“What are your early warning signs that you’re overloaded?” “What would help you feel back in control?”). Helps Daan 
translate stress into development actions (e.g., make a short task-overview, identify what to delegate, define a ‘signal early’ rule, 
plan how to catch up on training). Encourages ownership (e.g., “you choose what’s doable this week”) 
while offering scaffolding (e.g., buddy support, protected time, short weekly check-in). Summarizes a coaching plan 
with preparation tasks (e.g., write down obstacles/needs) and a scheduled follow-up to review what worked and adjust.
- **5** (Excellent): The candidate demonstrates high-impact, individualized coaching that helps Daan gain sharp insight 
into his patterns and converts that insight into self-owned development goals. They explicitly leverage Daan’s strengths 
as resources for change, while also naming growth areas. The candidate creates psychological space, 
adapts to what Daan is willing to share, and co-designs a concrete learning loop that respects autonomy and ensures progress.
*Example Behaviors*: Uses layered coaching questions (e.g., “What’s the first sign you’re slipping?” “What do you start doing/stop doing?” 
“What’s one small change this week that would make the biggest difference?”). Helps Daan formulate specific goals 
(e.g., “signal overload within 24h,” “attend/notify rule,” “complete system catch-up and practice with a buddy”) 
and choose strategies that fit him. Co-creates experiments (e.g., time-blocking, delegation script, meeting agenda input, 
stress-reduction routines) and builds accountability: date/time for follow-up, evidence to bring (e.g., task list, 
examples, reflections), and adjustment triggers if it doesn’t work. Closes by reinforcing capability 
(e.g., “you’ve done this before”) and commitment in Daan’s own words.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Coaching" competency.
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

    # --- Resultaatgerichtheid (Result orientation) ---
    "TM_RESUL": (
        "TM_RESUL",
        """
**Context of the role-playing exercise:**
You are a professional recruiter with extensive experience in evaluating job competencies from role-playing exercises. 
Your task is to evaluate a job candidate based on their responses in an asynchronous video role-playing exercise
comprised of four scenes. 

In this role-playing exercise, the candidate speaks with their employee Daan. Daan has been in the team 
for a few years and is generally known as positive and hardworking, but lately he has been less visible. 
He missed the weekly team meeting that morning without informing anyone. The team meeting is considered 
important because it is where plans for the coming week are discussed. The candidate has asked Daan 
to stop by to address what happened. More specifically:

- **Scene 1**: The conversation starts with Daan trying to avoid the topic and end it quickly because he is busy. 
He explains his absence as a deliberate choice, arguing the meeting often feels inefficient (unclear agenda, 
too much small talk) and saying he had other priorities (e.g., an important call). He also implicitly challenges 
the value of the meeting. The candidate should respond to Daan’s decision to skip the meeting without 
notice and his framing of the meeting as not worth his time.
- **Scene 2**: Daan partially acknowledges he should have been there, but immediately shifts to overload 
and reduced capacity. He describes having no peace at home or work, poor sleep, difficulty getting things done, 
and low energy. He reacts to the issue being raised as “making a fuss,” and asks to postpone: “Can’t we have 
this conversation another time?” The candidate should respond to Daan’s request to delay while also 
addressing the seriousness of the missed meeting and the signals of stress and disengagement.
- **Scene 3**:  Daan shares more detail about what is going on. He says his ex-partner is challenging 
the visitation arrangement for the kids, which is causing a lot of stress. He also mentions organizational changes 
and expresses frustration (e.g., “pffffffffff”), including a new system the team has to use that he finds difficult. 
He admits he missed the user training and says he doesn’t know how to handle everything right now. He asks directly: 
“Can you do something to help me?” The candidate should respond to Daan’s situation, including both the personal 
stressors and the work-related challenges (missed training, new system).
- **Scene 4**: Daan indicates he understands and thanks the candidate, but says he needs to get back to work soon. 
He asks for clarity and a recap: “So what exactly did we agree on, and what do you expect from me now?” 
The candidate should summarize the conversation, confirm any agreements made, and wrap up with clear expectations and next steps.

**Candidate Response**:
You are given the transcript of the candidate's full response across all four scenes below. 
Based on the candidate's transcribed text, evaluate the extent to which the candidate shows the following job competency.
Note that the text was automatically transcribed, so it may contain filler words, hesitation markers, partial sentences, 
and transcription glitches. Thus, evaluate the intended content instead of possible language mistakes due to transcription errors.

**Competency to evaluate:**  
**Result orientation** - The candidate’s ability for result-orientation skills, such as coming up with proposals on how Daan’s goals 
can be achieved more quickly or effectively, making clear agreements with Daan about the results to be achieved, or intervening 
and making timely adjustments when results are at risk of not being achieved.

**Evaluation Rubric & Behavioral Examples**:
Rate the candidate on a 1 to 5 scale based on the following criteria. 
Use the behavioral examples from similar transcripts to guide your rating.

- **1** (Insufficient): The candidate shows little to no result orientation. They do not translate the situation 
into clear result targets or concrete outcomes. Proposals are absent or purely generic, and the conversation lacks 
urgency when results are at risk. Agreements—if any—are vague. There is no monitoring plan 
and no contingency actions if problems recur.
*Example Behaviors*: Focuses mainly on empathy or general discussion without specifying what needs to improve 
(e.g., no clear expectation about notifying absence or attending the next meeting). Suggests broad intentions 
(e.g., “we’ll figure it out,” “let’s have coffee sometime”) rather than practical steps (e.g., task reprioritization, 
buddy/training catch-up, quick status update method). Avoids intervening when Daan tries to end the conversation 
or dismiss the meeting, allowing continued risk to team coordination. Ends without a concrete plan: no timeline 
for training, no short-term performance indicators (e.g., next two meetings attended/notified), 
no scheduled check-in, and no adjustment strategy if Daan misses again or falls further behind.
- **2** (Poor): The candidate shows some intention to protect results, but result orientation remains loosely defined. 
They do not consistently translate the situation into clear, measurable outcomes. Proposals tend to be generic 
and interventions are often delayed rather than immediate risk-control. Agreements—if present—lack specificity 
on who does what, by when, and how progress will be checked.
*Example Behaviors*: Emphasizes concern and asks what Daan needs, but does not set concrete targets 
(e.g., “next two meetings attended or notified beforehand”). Suggests a follow-up conversation or “making an overview,” 
yet no deliverables are defined (e.g., task list, delegation plan, availability for training). Mentions catching up on the missed 
system instruction/training, but without a firm timeline or success criterion (e.g., demonstrate use of the system on real tasks). 
Focuses on support and empathy, while leaving outcomes vague (e.g., “we’ll come back to this soon”). 
Ends without a clear checkpoint (date/time) or adjustment plan if Daan misses again.
- **3** (Sufficient): The candidate shows basic result orientation by translating the situation (missed team meeting without notice, 
overload, missed training/new system) into practical outcomes and near-term actions. They intervene in time, 
propose at least one concrete measure to reduce risk, and make reasonably clear agreements about what should improve 
(attendance/notice, training, workload overview). There is a follow-up moment or checkpoint, but goals and success criteria 
are only moderately specific.
*Example Behaviors*: Proposes a workable plan (e.g., create a priority list of tasks, identify what can be delegated), 
and schedule a catch-up training for the system (often with a buddy/colleague). Makes basic agreements (e.g., Daan should be present 
at the weekly meeting or notify in advance, and the manager will help arrange training/redistribute tasks). 
Sets a follow-up (e.g., “next week we sit down again”) and asks for concrete inputs (e.g., availability for training, 
list of tasks/overload points). Links actions to outcomes (e.g., less stress, fewer missed items, improved coordination), 
but may not specify measurable targets (e.g., “next 2 meetings attended/notified”) or explicit triggers for adjustments.
- **4** (Good): The candidate demonstrates clear, proactive result orientation by translating the situation into specific 
outcomes and a structured action plan. They intervene early when results are at risk (missed meeting without notice, 
overload, missed system training) and propose practical measures that speed up recovery. Agreements are clear 
and time-bound (who does what, by when), and the candidate introduces checkpoints to monitor progress and adjust quickly. 
Metrics may not be fully quantified, but expectations are operational and realistic.
*Example Behaviors*: Sets concrete near-term targets (e.g., “From now on, absence is communicated in advance,” 
“training is scheduled this week,” “we create a prioritized task list and reassign lower-priority work”). Proposes efficient 
interventions (e.g., dedicate an hour to sort tasks, assign a colleague/buddy for the new system, plan a catch-up session, 
and refine meeting structure, such as agenda or time-boxing to reduce wasted time). Builds monitoring into the plan 
(e.g., follow-up meeting next week, evaluation after training, and a trigger for adjustment if stress remains high or Daan 
misses another key moment). Concludes with a crisp summary of deliverables and timelines.
- **5** (Excellent): The candidate demonstrates strong, proactive result orientation by quickly translating Daan’s situation 
into clear, time-bound results for both performance and sustainability. They propose efficient, concrete interventions 
that accelerate progress and make SMART agreements: who does what, by when, and what “success” looks like. 
They intervene early when risk is visible, build in checkpoints, and specify adjustments if results slip. The close is crisp and action-focused.
*Example Behaviors*: Sets immediate deliverables (e.g., schedule the missed user training this week, identify a buddy for 
the system within one week, and attend the next team meeting or communicate early if not possible). Establishes 
a monitoring rhythm (e.g., weekly check-in / follow-up conversation) and defines triggers (e.g., “if it becomes too much, 
contact me immediately so we can adjust workload”). Proposes practical risk controls (e.g., temporary task redistribution, 
targeted support to reduce system-related delay, a clear timeline for reviewing progress). Summarizes agreements explicitly 
(e.g., training + buddy + escalation rule + follow-up date), ensuring Daan leaves with concrete next steps rather than general intentions.

**Evaluation Instructions**:
- Read the transcript of the job candidate's response (delimited between the triple backticks).
- Focus on verbal behaviors and the analytical content of the response that reflects 
the "Result orientation" competency.
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