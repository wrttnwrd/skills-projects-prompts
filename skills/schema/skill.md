---
name: schema-json-ld
description: Guidelines for creating schema markup for web pages
---

# When To Use This Skill

Use this skill for JSON+LD schema generation for web pages.

# How To Use This SKill

Whenever prompted to generate schema markup, JSON schema, or web page schema:

1. Rather than creating separate schema blocks for each property on a page, create hierarchical structure, where the main entity is described first, and then related secondary, tertiary and quaternary entites are nested within the main entity. 
2. Wherever possible, use the vocabulary - the types and properties - recognized by the schema.org specification. 
3. If no vocabulary exists, use simple, clear names for types and properties, with valud @context URLs
4. Carefully check syntax, generating JSON that will pass validation. 
5. Wrap generated schema in <script type="application/ld+json"> and </script>
6. If provided a URL, review that page before generating schema.