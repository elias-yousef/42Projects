/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 15:23:08 by eabushak          #+#    #+#             */
/*   Updated: 2026/01/08 12:13:24 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*findnewline(char *s)
{
	size_t	i;

	i = 0;
	if (!s)
		return (NULL);
	while (s[i])
	{
		if (s[i] == '\n')
			return (&s[i]);
		i++;
	}
	return (NULL);
}

char	*update_stash(char *stash)
{
	char	*nl;
	char	*new_stash;
	int		i;

	if (!stash)
		return (NULL);
	nl = findnewline(stash);
	if (nl == NULL)
		return (free(stash), NULL);
	i = ft_stringlen(nl);
	new_stash = malloc(sizeof(char) * (i + 1));
	if (new_stash == NULL)
		return (NULL);
	i = 0;
	while (nl[i] != '\0')
	{
		new_stash[i] = nl[i + 1];
		i++;
	}
	new_stash[i] = '\0';
	free(stash);
	return (new_stash);
}

char	*ft_strjoin(char *stash, char *buffer)
{
	size_t	len;
	size_t	i;
	size_t	j;
	char	*new;

	len = ft_stringlen(stash) + ft_stringlen(buffer);
	if (!stash)
	{
		stash = malloc(1);
		if (!stash)
			return (NULL);
		stash[0] = '\0';
	}
	new = malloc(sizeof(char) * (len + 1));
	if (!new)
		return (NULL);
	i = 0;
	j = 0;
	while (stash[i] != '\0')
		new[j++] = stash[i++];
	i = 0;
	while (buffer[i] != '\0')
		new[j++] = buffer[i++];
	new[j] = '\0';
	return (free(stash), new);
}
