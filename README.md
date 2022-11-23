# Laonzena school event matching system and web application.

## Plan

### Backend

-   Server

    -   [x] Create User
    -   [x] Update Information
    -   [ ] Matching
        -   [x] Matching Database Relationship
        -   [x] Waiting for Matching UP.
        -   [x] Admin Panel for matching inforamtion.
        -   [ ] Chatting with matched person (anonymously)

-   AI & ML
    -   [x] Cosine Similarity & Peason Correlation Similarity
    -   [ ] Information Latent Vector
    -   [ ] Neural Collaborative Recommendation
    -   [ ] Optimization for Production

### FrontEnd

-   UI

    -   [x] Home Page
    -   [x] Create User Page
    -   [x] User information Survey Page
    -   [x] Login for wathing matching status
    -   [x] User matching Page
    -   [ ] Chatting Page

## Theotreical Background

### Cosine Similarity

> In data analysis, cosine similarity is a measure of similarity between two sequences of numbers. [Learn More](https://en.wikipedia.org/wiki/Cosine_similarity)

$similarity=cos(Θ)=\frac{A⋅B}{||A||\ ||B||}=\frac{\sum_{i=1}^{n}{A_{i}×B_{i}}}{\sqrt{\sum_{i=1}^{n}(A_{i})^2}×\sqrt{\sum_{i=1}^{n}(B_{i})^2}}$

I thought that when I express the information of user in n-dimenstion, I can calculate the simliarity between the vector. I used cosine simliarity. I try to give a weight depending on the importance during matching. After some experiments, I had a several problems.

-   Weight didn't work well. As a result, it was matching between men and men.
-   The angle of two vector didn't represent that each users match well.

The conclusion is that cosine similarity doesn't correspond with my purpose.
