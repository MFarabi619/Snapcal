# Snapcal: University Event Tracking Simplified

University life offers a plethora of opportunities for students to build networks, discover new events, explore varied avenues, and enrich their knowledge beyond the classroom. Yet, an underlying challenge persists. Clubs and societies often grapple with efficiently consolidating their events onto a singular, accessible calendar for students. This inefficiency stems from a multitude of reasons — from architectural missteps, technical inadequacies, to inconsistent maintenance. As a consequence, students, already juggling demanding schedules, find themselves diving deep into myriad Instagram pages, sifting through numerous email lists, and laboriously entering event details into their personal calendars. This fragmented approach is not just tedious but also riddled with potential errors. What if there was a simpler and easier way to put events on your calendar?

## Table of Contents

- [Project Overview & Objective](#project-overview-&-objective)
- [Scope](#scope)
- [Technologies Used](#technologies-used)
- [Methodology](#methodology)
- [Benefits](#benefits)
- [Future Enhancements](#future-enhancements)
- [Team](#team)

## Project Overview & Objective

Snapcal aims to revolutionize this fragmented landscape. Imagine a scenario where, upon encountering an intriguing event poster or spotting an engaging Instagram advertisement, a student could simply capture the moment via a photo or screenshot. This image, when uploaded to Snap Schedule, undergoes data extraction, with all essential event details seamlessly integrated into the student's Google Calendar. The overarching objective is to craft a user-centric platform that not only alleviates the manual burdens on students but also empowers clubs and societies with a reliable tool to enhance event visibility and participation.

## Scope

1. **Capture**: Recognize event details from a variety of sources, such as physical posters, digital screenshots, or social media advertisements.
2. **Parse**: Extract essential details like event name, date, time, venue, and organizer details.
3. **Integrate**: Automatically populate the parsed event details into the student's Google Calendar.

## Technologies Used

- **OCR (Optical Character Recognition)**: To read and extract event details from images.
- **Front-End Web Frameworks (Svelte + SvelteKit)**: For building the user interface and web functionalities.
- **Backend Server (Node.js, Express.js)**: To process the image and extracted details.
- **Google Calendar API**: For integrating and adding events to the user's calendar.

## Methodology

1. **Image Upload**: Allow users to upload images or screenshots.
2. **Image Processing**: Use OCR to read the text and details from the uploaded image.
3. **Data Extraction**: Parse the extracted text to identify key event details.
4. **Integration**: Use Google Calendar API to populate the event details into the user's calendar.
5. **Review & Confirmation**: Before finalizing, let the user review and confirm the event details.

## Benefits

1. **Efficiency**: Students no longer need to manually input event details into their calendars.
2. **Comprehensiveness**: Capture event information from a multitude of sources, ensuring nothing is missed.
3. **Engagement**: Clubs, societies, and event organizers can reach a larger audience, ensuring better participation.

## Future Enhancements

1. **Web Scraping**: Provide the option to pase a link, so that a web-crawler can be used to extract event data.
2. **Social Media Integration**: Automatically detect and provide option to directly capture event details from platforms like Instagram or Facebook without needing screenshots.
3. **Recommendation System**: Suggest relevant events to users based on their past interests and engagements.
4. **Collaboration Tools**: Allow students to see which events their peers are attending, fostering community participation.

## Team

- **Rafi Khan**: Back-End Developer & Integrations Specialist
- **Mumtahin Farabi**: UI/UX Designer & Front-End Developer
  

