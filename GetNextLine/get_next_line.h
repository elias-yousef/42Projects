/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/22 13:20:07 by eabushak          #+#    #+#             */
/*   Updated: 2026/01/08 12:26:49 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42

# endif

# include <unistd.h>
# include <stdlib.h>

int		ft_stringlen(char *str);
char	*ft_line(char *stash);
char	*read_file(int fd, char *stash);
char	*get_next_line(int fd);
char	*findnewline(char *s);
char	*update_stash(char *stash);
char	*ft_strjoin(char *stash, char *buffer);

#endif
