---
name: schema-json-ld
description: Guidelines for creating schema markup for web pages
---

# When To Use This Skill

Use this skill for JSON+LD schema generation for web pages.

# How To Use This Skill

Whenever prompted to generate schema markup, JSON schema, or web page schema, follow these guidelines:

## Core Principles

1. **Hierarchical Structure**: Rather than creating separate schema blocks for each property on a page, create hierarchical structure, where the main entity is described first, and then related secondary, tertiary and quaternary entities are nested within the main entity.

2. **Schema.org Vocabulary**: Wherever possible, use the vocabulary - the types and properties - recognized by the schema.org specification.

3. **Fallback Naming**: If no schema.org vocabulary exists, use simple, clear names for types and properties.

4. **Syntax Validation**: Carefully check syntax, generating JSON that will pass validation.

5. **Proper Wrapping**: Wrap generated schema in `<script type="application/ld+json">` and `</script>`

6. **URL Review**: If provided a URL, review that page before generating schema.

## @context Declaration

Always include the @context at the root level:
```json
{
  "@context": "https://schema.org",
  "@type": "TypeName",
  ...
}
```

For multiple entities in one script block, use an array:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", ... },
    { "@type": "WebSite", ... }
  ]
}
```

## Common Schema Types

Familiarize yourself with frequently used types:

- **Organization**: Companies, brands, institutions
- **Person**: Individual people
- **Product**: Items for sale
- **Article**: News articles, blog posts
- **LocalBusiness**: Physical business locations
- **WebPage**: Individual web pages
- **WebSite**: Entire websites
- **BreadcrumbList**: Navigation breadcrumbs
- **FAQPage**: FAQ pages
- **HowTo**: Step-by-step instructions
- **Review**: User reviews and ratings
- **AggregateRating**: Combined ratings
- **Event**: Events and happenings
- **Recipe**: Cooking recipes
- **VideoObject**: Video content
- **ImageObject**: Images
- **Service**: Services offered
- **JobPosting**: Job listings

## Universal Properties

These properties are applicable to almost all types:

- **name**: The name of the entity (almost always required)
- **url**: The URL of the entity (strongly recommended)
- **image**: An image URL or ImageObject (recommended)
- **description**: A description of the entity (recommended)
- **@id**: A unique identifier for the entity (useful for referencing)

## Required vs Recommended Properties

### For Products:
**Required**: name, image, offers (with price and availability)
**Recommended**: description, brand, review, aggregateRating, sku

### For Articles:
**Required**: headline, image, datePublished, dateModified
**Recommended**: author, publisher (with logo), articleBody

### For LocalBusiness:
**Required**: name, address, telephone
**Recommended**: image, url, openingHours, priceRange, geo

### For Events:
**Required**: name, startDate, location
**Recommended**: description, image, offers, performer, endDate

### For Reviews:
**Required**: reviewRating, author, reviewBody (or name)
**Recommended**: datePublished, itemReviewed

## Data Formatting Standards

- **Dates**: Use ISO 8601 format
  - Date only: `YYYY-MM-DD` (e.g., "2025-10-20")
  - Date and time: `YYYY-MM-DDTHH:MM:SS` (e.g., "2025-10-20T14:30:00")
  - With timezone: `YYYY-MM-DDTHH:MM:SS-07:00` or `YYYY-MM-DDTHH:MM:SSZ`

- **URLs**: Always use absolute URLs
  - ✓ Good: "https://example.com/page"
  - ✗ Bad: "/page" or "page.html"

- **Images**: Provide full URL with dimensions when possible
  ```json
  "image": {
    "@type": "ImageObject",
    "url": "https://example.com/image.jpg",
    "width": 1200,
    "height": 800
  }
  ```

- **Phone Numbers**: Use international format when possible
  - "+(country code)(area code)(number)"
  - Example: "+1-415-555-1234"

- **Prices**: Always include currency
  ```json
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "USD"
  }
  ```

## Multiple Schemas Guidance

### When to use separate script blocks:
- When schemas represent completely independent entities
- For different page types (e.g., Article + Organization)

### When to nest within one schema:
- When entities are related (e.g., Product contains Review)
- When one entity is a property of another (e.g., Organization contains Person as employee)

### Using arrays for multiple items:
```json
"review": [
  {
    "@type": "Review",
    "author": "John Doe",
    ...
  },
  {
    "@type": "Review",
    "author": "Jane Smith",
    ...
  }
]
```

## Referencing Entities with @id

Use @id to reference entities without duplicating data:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Corp"
    },
    {
      "@type": "Article",
      "publisher": {
        "@id": "https://example.com/#organization"
      }
    }
  ]
}
```

## Error Handling

- **Missing optional properties**: Omit them entirely rather than using null
- **Missing required properties**: 
  - If truly unavailable, note this to the user
  - Consider using a more general type that doesn't require that property
- **Uncertain data**: Don't guess - ask the user or omit the property

## Validation Tools

After generating schema, recommend these validation tools:

1. **Google Rich Results Test**: https://search.google.com/test/rich-results
   - Best for checking Google Search compatibility
   - Shows how Google will interpret the markup

2. **Schema Markup Validator**: https://validator.schema.org/
   - Official schema.org validator
   - Checks syntax and structure

3. **JSON-LD Playground**: https://json-ld.org/playground/
   - Useful for testing and debugging JSON-LD

## Common Patterns

### Organization with Logo:
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Company",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  }
}
```

### Article with Author and Publisher:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "image": "https://example.com/image.jpg",
  "datePublished": "2025-10-20",
  "dateModified": "2025-10-20",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Example Company",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
```

### BreadcrumbList:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Category",
      "item": "https://example.com/category"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Current Page",
      "item": "https://example.com/category/page"
    }
  ]
}
```

## Best Practices

1. **One schema per logical entity**: Don't try to cram everything into one type
2. **Use specific types**: Choose the most specific applicable type (e.g., LocalBusiness > Organization)
3. **Provide rich data**: Include as many relevant properties as available
4. **Keep it accurate**: Only include data that appears on the page
5. **Test thoroughly**: Always validate before deployment
6. **Update regularly**: Keep schema current with page content changes
7. **Consider user intent**: Think about what information search engines and users need most

## Output Format

Always present the final schema wrapped in proper script tags:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TypeName",
  "property": "value"
}
</script>
```

For multiple related schemas, you can either use separate script blocks or combine with @graph:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Type1", ... },
    { "@type": "Type2", ... }
  ]
}
</script>
```